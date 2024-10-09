from telebot import types, TeleBot
from dotenv import load_dotenv 
import os
import random
load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("Камень")
    key2 = types.KeyboardButton("Ножницы")
    key3 = types.KeyboardButton("Бумага")
    keyboard.add(key1, key2, key3)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! Поиграем? Выбери: камень, ножницы, бумага', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def play_game(message):
    #keyboard = types.InlineKeyboardMarkup() 
    #key1 = types.InlineKeyboardButton(text='Камень', callback_data='Камень')
    #key2 = types.InlineKeyboardButton(text='Ножницы', callback_data='Ножницы') 
    #key3 = types.InlineKeyboardButton(text='Бумага', callback_data='Бумага') 
    #keyboard.add(key1)
    #keyboard.add(key2)
    #keyboard.add(key3)
    
    user_choice = message.text.lower()
    choices = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(choices)
    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or (user_choice == 'ножницы' and bot_choice == 'бумага') or (user_choice == 'бумага' and bot_choice == 'камень'):
        result = "Вы выиграли!"
    else:
        result = "Я выиграл!"
    bot.send_message(message.chat.id, f"Вы выбрали {user_choice}, я выбрал {bot_choice}. {result}")

bot.polling(none_stop=True, interval=0)


