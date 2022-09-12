# MockingBot

![Mocking Spongebob](./Mocking-Spongebob.jpg)

A basic serverless [Telegram bot](https://core.telegram.org/bots) using [Google Cloud Functions](https://cloud.google.com/functions/).

[Add this to your group](https://t.me/M0cking_Bot) and type `/mock` or `/uwu` followed by your message, or simply use `@M0cking_Bot` for DMs. Contact [@incomple](https://t.me/Incomple) for feedback and suggestions.

This bot runs with Python 3.7 and [python-telegram-bot](https://python-telegram-bot.org/).

Adapted from Pablo Seminario's repo: <https://github.com/pabluk/serverless-telegram-bot>

See https://seminar.io/2018/09/03/building-serverless-telegram-bot/ for more details about this bot.

## Deploy

```
$ gcloud beta functions deploy webhook --set-env-vars "TELEGRAM_TOKEN=000:yyy" --runtime python37 --trigger-http
```

## Testing

```
$ pip install -r requirements-test.txt
$ python test_main.py
```
