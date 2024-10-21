from telebot import types, TeleBot
from dotenv import load_dotenv 
import os
load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def get_start(massege):
    bot.send_message(massege.from_user.id, 'привет')

@bot.message_handler(commands=['help'])
def get_help(massege):
    bot.send_location(chat_id=['123'])

bot.polling(non_stop=True)