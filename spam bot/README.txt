# Telegram Spam Bot (Educational Example)

This repository contains a simple Python script that demonstrates how to use the [Telegram Bot API](https://core.telegram.org/bots/api) to send repeated messages to a chat.  
 **Important:** This is for **educational purposes only**. Do **not** use it to harass, spam, or attack others. Misuse can get your bot banned.


##Requirements

- Python 3.x
- The [`requests`](https://pypi.org/project/requests/) library

Install dependencies with:

```bash
pip install requests

NOW :

Create a new bot using @BotFather
 on Telegram:

Run /newbot

Give your bot a name 

Copy the API Token

Get your chat ID

Add the bot to a group or start a private chat with it

Send any message

Open this link in your browser (replace YOUR_TOKEN):

https://api.telegram.org/botYOUR_TOKEN/getUpdates

Look for "chat": { "id": ... } → copy the number (that’s your chat ID)

Create a config.py file in the repo root (never commit this file):

TOKEN = "your-telegram-bot-token"
CHAT_ID = -1234567890  # your chat ID (negative for groups)

Run the script:
python spam.py

DISCLAIMER !!

Do not hardcode your private token in public code.

Do not use this script to spam others.

This repository is for educational/demo purposes only.

Misuse may result in your bot being blocked by Telegram.

BY SNEAKID:: 
ENJOY :)