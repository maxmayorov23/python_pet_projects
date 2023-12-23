import telebot

API_TOKEN = '6408579321:AAFCNEkjbsIydN-hbncO_GJw3CSTIs9fmxU'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
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
""")

@bot.message_handler(commands=['hobbies'])
def send_welcome(message):
    bot.reply_to(message, """\
Я люблю играть в компьютерные игры, увлекаюсь страйкболом, изучаю Питон.\
""")\

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if (message.text == "привет" or message.text == "Привет"):
        bot.reply_to(message, f"Привет, {message.from_user.first_name}. Рад тебя видеть!")


bot.infinity_polling()
