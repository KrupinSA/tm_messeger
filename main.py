import os
import requests
import telegram
import textwrap
import time


DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
WAITING_TIME = 91

url = 'https://dvmn.org/api/long_polling/'

headers = {
    "Authorization": 'Token {}'.format(DEVMAN_TOKEN)
}

bot = telegram.Bot(token=TG_TOKEN)
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
            bot.send_message(CHAT_ID, text=text)
    connection_error_count = 0
        
  except requests.exceptions.ReadTimeout: pass
  except requests.exceptions.ConnectionError: 
      if connection_error_count == 5:
          time.sleep(600)
          continue
      connection_error_count += 1
