import os
import telebot

class Bot:
    def __init__(self):
        self.token = os.environ.get('TG_TOKEN')
        self.user_id = int(os.environ.get('TG_USER_ID'))
        self.bot = telebot.TeleBot(self.token)

        
    def send_graph(self, image):
        self.bot.send_photo(self.user_id, image)

    def send_text(self, text):
        self.bot.send_message(self.user_id, text)
 
    def send_file(self, file):
        self.bot.send_document(self.user_id, file)

    def send_results(self, text, image, file):
        self.bot.send_message(self.user_id, text)
        self.bot.send_photo(self.user_id, image)
        self.bot.send_document(self.user_id, file)






    
