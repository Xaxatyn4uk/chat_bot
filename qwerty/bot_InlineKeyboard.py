from telebot import types, TeleBot
from dotenv import load_dotenv 
from key_button import keyboard2
import os
load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))

@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    bot.send_message(call.message.chat.id, f'вы нажали {call.data}')

@bot.message_handler(commands=['start'])
def get_start(massege):
    bot.send_message(massege.from_user.id, 'привет', reply_markup=keyboard2)

bot.polling(non_stop=True)
 