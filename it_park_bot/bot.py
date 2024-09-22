import telebot;
bot = telebot.TeleBot('7002682336:AAFKLNJj93CmNFepx5145-x7x6FWho93wQ0'); #тут токен бота
name = ''
age = 0
@bot.message_handler(content_types=['text']) #слушаем бота
def get_text(message):
    if message.text == "Привет": #проверям сообщение от пользователя
        bot.send_message(message.from_user.id, "Привет Друг! Как тебя зовут?") #отвечаем пользователю
        bot.register_next_step_handler(message, get_name)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'{name} сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    age = int(message.text)
    bot.send_message(message.from_user.id, f'{name} вы {2024 - age} года рождения')

bot.polling(none_stop=True, interval=0)# бот постоянно будет опрашивает сервер