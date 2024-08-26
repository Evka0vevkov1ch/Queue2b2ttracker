import time
import re
import asyncio
from telegram import Bot
from telegram.error import NetworkError, TelegramError
from telegram.ext import Application
from config import LOG_FILE_PATH, TELEGRAM_TOKEN, CHAT_ID
app = Application.builder().token(TELEGRAM_TOKEN).build()

def parse_queue_position(line):
    match = re.search(r'Position in queue:\s*(\d+)', line)
    if match:
        return match.group(1)  
    return None
def get_latest_queue_position():
    try:
        with open(LOG_FILE_PATH, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                position = parse_queue_position(line)
                if position:
                    return position
    except FileNotFoundError:
        print("Log file not found.")
    return None
async def send_message(message):
    try:
        await app.bot.send_message(chat_id=CHAT_ID, text=message)
    except TelegramError as e:
        print(f"An error occurred: {e}")
async def main():
    last_position = None

    while True:
        position = get_latest_queue_position() 
        if position and position != last_position:
            message = f"Position in queue: {position}"
            await send_message(message)  
            last_position = position
        elif not position:
            print("No queue position found.")  

        await asyncio.sleep(5)  

if __name__ == "__main__":
    asyncio.run(main())
