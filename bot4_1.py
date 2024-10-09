from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv 
import os

load_dotenv()
Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data == 'yes')
async def press_button(callback_query: types.callback_query):
    await callback_query.answer.mess

@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    inline_key = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardMarkup('yes')
    key2 = types.InlineKeyboardMarkup('no')
    inline_key.add(key1, key2)
    await message.answer('давай поиграем')

@dp.message_handler(commands=['help'])
async def help_command(messege: types.message):
    await messege.answer(
        """я бот эхо
напиши мне что нибудь"""
    )

@dp.message_handler()
async def send_message(message: types.message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)