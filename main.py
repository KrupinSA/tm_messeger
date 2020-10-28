import os
import requests
import telegram
import textwrap
import time
import logging
from telegram.ext import Updater


DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
WAITING_TIME = 91

main_logger = logging.getLogger(__name__)


class TelegHandler(logging.Handler):
    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id
        
    def emit(self, record):
        log = self.format(record)
        self.bot.send_message(self.chat_id, log)


def main_loop(bot, dispatcher):
    url = 'https://dvmn.org/api/long_polling/'

    headers = {
        "Authorization": f'Token {DEVMAN_TOKEN}'
    }

    params = {}
    connection_error_count = 0
        
    while True:
        try:
            response = requests.get(url, headers=headers, params=params, timeout=WAITING_TIME)
            response.raise_for_status()
            response_content = response.json()
            if 'error' in response_content:
                raise requests.exceptions.HTTPError(response_content['error'])
            if response_content['status'] == 'timeout':
                params = {'timestamp': response_content['timestamp_to_request']}
                continue
            if response_content['status'] == 'found':
                params = {'timestamp': response_content['last_attempt_timestamp']} 
                for attempt in response_content['new_attempts']:
                    text = '''\
                    У вас проверили работу "{}"
                    https://dvmn.org{}
                    '''
                    text = text.format(attempt['lesson_title'],
                                    attempt['lesson_url'],
                                    )
                    if attempt['is_negative']:
                        text += 'К сожалению, в работе нашлись ошибки.'
                    else:
                        text += 'Преподователю все понравилось, можно приступать к следующему уроку!'
                    text = textwrap.dedent(text)
                    bot.send_message(TELEGRAM_CHAT_ID, text=text)
            connection_error_count = 0
                
        except requests.exceptions.ReadTimeout: pass
        except requests.exceptions.ConnectionError: 
            if connection_error_count == 5:
                time.sleep(600)
                continue
            connection_error_count += 1
        except telegram.error.TelegramError as err:
            main_logger.error(err)
            dispatcher.logger.error("Bot произошла ошибка")
            dispatcher.logger.error(err, exc_info=True)


def main():
    message_format = "%(asctime)s:[%(name)s]%(filename)s.%(funcName)s:%(levelname)s:%(message)s"
    bot_message_format = "%(message)s"
    level = logging.INFO

    # Init logging to console
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(message_format)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    main_logger.addHandler(console_handler)

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    main_logger.warning("Bot запущен")

    # Init ligging to telegram
    telegram_handler = TelegHandler(bot, TELEGRAM_CHAT_ID)
    formatter = logging.Formatter(bot_message_format)
    telegram_handler.setFormatter(formatter)
    telegram_handler.setLevel(level)
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.logger.addHandler(telegram_handler)

    dispatcher.logger.warning("Bot запущен")

    main_loop(bot, dispatcher)

if __name__ == "__main__":
    main()
 
