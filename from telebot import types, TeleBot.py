from telebot import TeleBot

bot = TeleBot('7722176687:AAEMdlgdfRPzPExPmub2SFqXt9eGRqz1f0c')

name = ''
age = 0
@bot.message_handler(content_types=['text'])
def get_start(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, Друг! Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.next == "/start":
        bot.send_message(message.from_user.id, "напиши: Привет")
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'{name} сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    global age
    age = int(message.text)
    bot.send_message(message.from_user.id, f'{name}, вы {2024-age} год рождения')
    bot.register_next_step_handler(message, get_start)

bot.polling(none_stop=True, interval=0)