import requests
import threading

TOKEN = "your private token"  # get it from @BotFather
CHAT_ID = "your id here" #check readme file 
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def spam():
    while True:
        requests.post(URL, data={"chat_id": CHAT_ID, "text": "hello word"}) #<<<<< change hello word to your message spam  \\ enjoy :)

for _ in range(10):
    t = threading.Thread(target=spam)
    t.start()