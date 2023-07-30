import requests
import json

class Telegram:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def sendMessage(self, msg):
        requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(self.token, self.chat_id, msg))