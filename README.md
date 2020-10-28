# tm_messenger

<<<<<<< HEAD
The service is designed to notify in telegram about checking works on courses https://dvmn.org

## Environment

### Requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```sh
pip install -r requirements.txt
```

### Environment variables

- SECRETS_KEY

```sh
export TELERAM_TOKEN="......"

export TELEGRAM_CHAT_ID="......"

export DEVMAN_TOKEN="....."
```
#### How to get

* Follow the link for instructions on how to get a telegram token. https://core.telegram.org/bots#6-botfather

## Run

Launch on Linux(Python 3) or Windows:

```sh
$ python main.py
```
=======
Сервис предназначен для оповещения в telegram о проверке работ по курсам https://dvmn.org

Первоначально необходимо получить токены.

По ссылке можно ознакомиться с инструкцией по получению токена для telegram. https://core.telegram.org/bots#6-botfather

Для работы сервиса необходим python3.8 и выше.

Устанавливаем необходимые модули

```sh
pip3 install -r requirements.txt
```

Экспортируем токен telegram в переменную окружения.

```sh
export TG_TOKEN="......"
```

Экспортируем id чата

```sh
export CHAT_ID="......"
```

Экспортируем токен devman.org 

```sh
export DEVMAN_TOKEN="....."
```

запуск python3 main.py



>>>>>>> 3d610e3e4582ad7196d4e43e926038fe0bfa7cfe
