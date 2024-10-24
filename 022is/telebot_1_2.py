from telebot import types, TeleBot
import random

bot = TeleBot('7002682336:AAFKLNJj93CmNFepx5145-x7x6FWho93wQ0')

@bot.message_handler(commands=['start'])
def 