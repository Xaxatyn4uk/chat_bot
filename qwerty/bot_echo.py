from telebot import types, TeleBot
from dotenv import load_dotenv 
import os
load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))

@bot.message_handler(content_tepes=['start'])
def get_start(massege):
    bot.send_message(massege.from_user.id, massege.text)

bot.polling(non_stop=True)