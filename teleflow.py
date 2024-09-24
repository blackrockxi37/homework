import os
import telebot

class Bot():
    def __init__(self):
        self.token = os.environ.get('TOKEN')
        self.user_id = os.environ.get('USER_ID')
        self.bot = telebot.TeleBot(self.token)
        
    def send_graph(self, image):
        self.bot.send_photo(self.user_id, image)

    def send_text(self, text):
        self.bot.send_message(self.user_id, text)

    def send_file(self, file):
        self.bot.send_document(self.user_id, file)


    
