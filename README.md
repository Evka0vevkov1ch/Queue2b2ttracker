On eng:
1. Introduction
This project is designed for monitoring queue positions based on logs and sending notifications to Telegram. The script automatically tracks changes in the log file and sends a message with the new queue position to the specified Telegram chat.

2. Installing Python
Before you start, ensure that Python version 3.7 or higher is installed on your computer.

To check if Python is installed and what version is being used, run the following command in your command line:


in cmd: python --version

If Python is not installed, download it from the official website and follow the installation instructions.

3. Installing Dependencies
The project uses the python-telegram-bot library. Install it using pip by running the following command in your command line:


in cmd: pip install python-telegram-bot==20.0

4. Creating a Telegram Bot via BotFather
To enable the bot to send messages, you need to create it on Telegram:

1. Open Telegram and find the user @BotFather.
2. Send /start to begin interaction.
3. Send /newbot to create a new bot.
4. Follow the instructions to choose a name and username for your bot.
5. After successful creation, BotFather will send you a token.
Now open the config.py file and insert this token into the TELEGRAM_TOKEN variable to allow your bot to send messages:

TELEGRAM_TOKEN = 'your_bot_token'

5. 1. Obtaining Chat ID
   2. To obtain your Chat ID, follow these steps:

Find the bot @userinfobot on Telegram and start a chat with it.
The bot will send information about your account, including your Chat ID, in response to any message.
Add this Chat ID to the config.py file in the CHAT_ID variable:


CHAT_ID = 'your_chat_id'

6. Configuring the Log File Path
The log file you want to monitor should be located in the logs folder within the game directory. Specify the path to this file in the LOG_FILE_PATH variable in config.py.

The log file is always named latest.log, so the path should look like this:


LOG_FILE_PATH = 'C:/path_to_your_game/logs/latest.log'

7. Running the Script
After you have configured all necessary parameters in the config.py file, follow these steps to run the script:

1. Open the folder containing the main.py file.

2. Right-click on the folder while holding the Shift key and select the option Open PowerShell window here or Open Command Prompt here (depending on your Windows version).

3. In the opened console, enter the following command:

in cmd: python main.py

4. Ensure that the bot is running and check that it starts monitoring the log file and sending notifications to your Telegram chat.

If you haven't done so already, open Telegram, find your bot, and send the command /start. This will establish basic communication with the bot and enable it to send messages.


On rus:
1. Введение
Этот проект предназначен для мониторинга позиции в очереди на основе логов и отправки уведомлений в Telegram. Скрипт автоматически отслеживает изменения в лог-файле и отправляет сообщение с новой позицией в очереди в указанный Telegram-чат.

2. Установка Python
Перед началом работы убедитесь, что на вашем компьютере установлен Python версии 3.7 или выше.

Чтобы проверить, установлен ли Python и какая версия используется, выполните в командной строке:


в cmd: python --version
Если Python не установлен, загрузите его с официального сайта и следуйте инструкциям по установке.

3. Установка зависимостей
В проекте используется библиотека python-telegram-bot. Установите её с помощью pip. Для этого выполните в командной строке:


в cmd: pip install python-telegram-bot==20.0

4. Создание бота в Telegram через BotFather
Чтобы бот мог отправлять сообщения, необходимо создать его в Telegram:

1. Откройте Telegram и найдите пользователя @BotFather.
2. Напишите /start, чтобы начать взаимодействие.
3. Напишите /newbot, чтобы создать нового бота.
4. Следуйте инструкциям для выбора имени и username для бота.
5. После успешного создания BotFather отправит вам токен.
Теперь откройте файл config.py и вставьте этот токен в переменную TELEGRAM_TOKEN, чтобы ваш бот мог отправлять сообщения:

Пример: TELEGRAM_TOKEN = 'ваш_токен_бота'

5. Получение Chat ID
Для получения вашего Chat ID выполните следующие шаги:

1. Найдите в Telegram бота @userinfobot и начните с ним диалог.
2. В ответ на любое сообщение бот отправит информацию о вашем аккаунте, включая ваш Chat ID.
Этот Chat ID также нужно добавить в файл config.py в переменную CHAT_ID:

Пример: CHAT_ID = 'ваш_chat_id'

6. Настройка пути к файлу логов
Файл логов, который вы хотите отслеживать, должен находиться в папке logs, которая расположена в директории игры. Укажите путь к этому файлу в переменной LOG_FILE_PATH в config.py.

Файл лога всегда называется latest.log, поэтому путь к нему будет выглядеть так:

Пример: LOG_FILE_PATH = 'C:/path_to_your_game/logs/latest.log'
7. Запуск скрипта
После того как вы настроили все необходимые параметры в файле config.py, выполните следующие шаги для запуска скрипта:

1. Откройте папку с файлом main.py.

2. Щёлкните правой кнопкой мыши по этой папке, удерживая клавишу Shift, и выберите опцию Открыть окно PowerShell здесь или Открыть окно командной строки здесь (в зависимости от версии Windows).

3. В открывшейся консоли введите команду:

В cmd: python main.py
4. Убедитесь, что бот запущен, и проверьте, что он начал отслеживать лог-файл и отправлять уведомления в ваш Telegram-чат.

Если вы ещё не сделали это, откройте Telegram, найдите вашего бота и отправьте команду /start. Это установит с ботом базовую связь и позволит ему отправлять сообщения.
