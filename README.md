# tm_messenger
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
