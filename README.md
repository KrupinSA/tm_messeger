# tm_messenger

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



