from telebot import types, TeleBot
from dotenv import load_dotenv 
from key_button import keyboard
import os
load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def get_start(massege):
    bot.send_message(massege.from_user.id, 'привет', reply_markup=keyboard)

#@bot.message_handler(content_types=['text'])
#def send_text(message):
#    if message.text == 'да':
#        bot.send_message(message.from_user.id, 'вы нажали да')
#   elif message.text == 'нет':
#        bot.send_message(message.from_user.id, 'вы нажали нет')
#   else:
#        bot.send_message(message.from_user.id, 'нажмите на кнопки')



@bot.message_handler(func=lambda message: message.text == 'да') #декоратор
def send_text(message):
    bot.send_message(message.from_user.id, f'вы нажали"{message.text}"', 
                     reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(func=lambda message: True)
def send_text(message):
    bot.send_message(message.from_user.id, f'вы набрали"{message.text}"', 
                     reply_markup=types.ReplyKeyboardRemove())


bot.polling(non_stop=True)