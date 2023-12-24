'''
Телеграм бот: Личная визитка

https://pytba.readthedocs.io/en/latest/quick_start.html
'''

import telebot
from telebot import types
API_TOKEN = '6408579321:AAFCNEkjbsIydN-hbncO_GJw3CSTIs9fmxU'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Добро пожаловать в бот визитку!
Для вызова справки нажмите /help
""")

@bot.message_handler(commands=['about'])
def send_welcome(message):
    bot.reply_to(message, """\
Это моя электронная визитка в телеграм боте, которая поможет вам узнать обо мне.\
""")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Бот поддерживает следующие команды: 
/start
/help
/about 
/hobbies

Так же бот может отвечать вам на сообщение: "Привет" или "привет"
""")

@bot.message_handler(commands=['hobbies'])
def send_welcome(message):
    bot.reply_to(message, """\
Я люблю играть в компьютерные игры, увлекаюсь страйкболом, изучаю Питон.\
""")
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_1 = types.InlineKeyboardButton(text="GitHub", url="https://github.com/maxmayorov23")
    markup.add(btn_1)
    bot.send_message(message.chat.id, "Тут вы можете посмотреть мой GitHub", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if (message.text == "привет" or message.text == "Привет"):
        bot.reply_to(message, f"Привет, {message.from_user.first_name}. Рад тебя видеть!")

if __name__=="__main__":
    bot.infinity_polling(none_stop=True)
