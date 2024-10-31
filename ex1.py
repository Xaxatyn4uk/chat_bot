from telebot import types
import telebot

token = '7002682336:AAFKLNJj93CmNFepx5145-x7x6FWho93wQ0'
my_chat_id = '770139693'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Услуги')
    button2 = types.KeyboardButton(text='О нас')
    button3 = types.KeyboardButton(text='Оставить заявку')
    button4 = types.KeyboardButton(text='Меню')
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, f'Привет {message.from_user.username}, добро пожаловать', reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'о нас':
        info_func(message)
    if message.text.lower() == 'оставить заявку':
        bot.send_message(message.chat.id, 'Оставьте свои контактные данные')
        bot.register_next_step_handler(message, send_reqest)
    if message.text.lower() == 'услуги':
        servive(message)
    if message.text.lower() == 'меню':
        menu(message)

    

def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='перейти на сайт', url='https://itpark.tech/')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку', reply_markup=keyboard)

def send_reqest(message):
    mes=f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо за заявку, С вами скоро свяжутся!')

def servive(message):
    bot.send_message(message.chat.id, '1 услуга')
    bot.send_message(message.chat.id, '2 услуга')
    bot.send_message(message.chat.id, '3 услуга')

def menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text='Отправить номер телефона', request_contact=True)
    button_geo = types.KeyboardButton(text='Отправить местоположение', request_location=True)
    button_back = types.KeyboardButton(text='Назад')
    keyboard.add(button_phone)
    keyboard.add(button_geo)
    keyboard.add(button_back)
    bot.send_message(message.chat.id, 'Отправь мне свой телефон или поделись местоположением', reply_markup=keyboard)
    




if __name__=='__main__':
    bot.infinity_polling()