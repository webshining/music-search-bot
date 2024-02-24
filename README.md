# <p align="center">Aiogram Mongo Template</p>

### <p align="center"><a href="https://core.telegram.org/bots/api">Telegram Bot</a> template with <a href="https://docs.aiogram.dev/en/dev-3.x/">aiogram</a>, <a href="https://www.mongodb.com/">mongodb</a> and <a href="https://www.docker.com/">docker</a></p>

## Technologies used:

- Aiogram
- Redis
- i18n
- Docker and docker compose

## Navigate

- [Getting started](#getting-started)
    - [Init project](#init-project)
    - [Configure environment variables](#configure-environment-variables)
        - [Bot config](#bot-config)
        - [Redis config](#redis-config)
        - [Database config](#database-config)
    - [Application start (local)](#application-start-local)
- [Docker](#docker)
    - [Application start (docker)](#application-start-docker)
    - [View app logs](#view-app-logs)
    - [Rebuild](#rebuild)

## Getting started

### Init project

```bash
$ git clone https://github.com/webshining/holychords-bot project_name
$ cd project_name
$ pip install -r requirements.txt
```

### Configure environment variables

> Copy variables from .env.ren file to .env

```bash
$ cp .env.ren .env
```

### Bot config

`TELEGRAM_BOT_TOKEN` - your bot token (required)

### Redis config

> If you are not using redis, by default used MemoryStorage

`RD_DB` = redis database (number)

`RD_HOST` = redis host

`RD_PORT` = redis port

`RD_URI` - connection url to your redis server

### Application start (local)

```bash
$ python main.py
# If you have make you can enter
$ make run
```

## Docker

### Application start (docker)

> Run only one service:<br>
> ```bash
> $ docker-compose up -d service_name
> # If you have make you can enter
> $ make rebuild service_name
> ```

```bash
$ docker-compose up -d
# If you have make you can enter
$ make rebuild
```

### View app logs

```bash
$ docker-compose logs -f app
# If you have make you can enter
$ make logs
```

### Rebuild

```bash
$ docker-compose up -d --build --no-deps --force-recreate
# If you have make you can enter
$ make rebuild
```
