'''
Телеграм бот: Анкета (Quiz) пользователя

В данном "квизе" будут проверяться базовые знания физики 7 класса
'''

import telebot
from telebot import types
API_TOKEN = '6408579321:AAFCNEkjbsIydN-hbncO_GJw3CSTIs9fmxU'

bot = telebot.TeleBot(API_TOKEN)

questions = {
    "1": {
        "question": "В чем измеряется длина?",
        "answer": {
            "1": "в метрах",
            "2": "в килограммах",
            "3": "в молях"
        }
    },
    "2": {
       "question": "Какой формулой измеряется пройденное расстояние?",
        "answer": {
            "1": "S = v * t",
            "2": "D = S * v",
            "3": "Такой формулы не существует"
        }
    },
    "3": {
        "question": "Чему равно  ускорение свободного падения?",
        "answer": {
            "1": "g = 9,806 65 м/с2",
            "2": "g = 1",
            "3": "g = 3.14"
        }
    }
}

is_continue = False

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}. Добро пожаловать в наш 'квиз' по физике! Давай проверим твои знания за 7-ой класс😉 Для вызова справки нажми /help Для начала тестирования введи /test")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Как пользоваться ботом:
тебе будет предложено 3 вопроса с вариантами ответа.
После прохождения теста ты узнаешь свою оценку.
""")

@bot.message_handler(commands=['test'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn_1 = types.InlineKeyboardButton(text=questions["1"]["answer"]["1"], callback_data="btn1")
    btn_2 = types.InlineKeyboardButton(text=questions["1"]["answer"]["2"], callback_data="btn2")
    btn_3 = types.InlineKeyboardButton(text=questions["1"]["answer"]["3"], callback_data="btn3")
    markup.add(btn_1, btn_2, btn_3)
    bot.send_message(message.chat.id, questions["1"]["question"], reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "btn1":
        bot.send_message(call.message.chat.id, "Это правильный ответ")
        global is_continue
        is_continue = True
    elif call.data == "btn2":
         bot.send_message(call.message.chat.id, "Попробуй еще раз")
    elif call.data == "btn3":
         bot.send_message(call.message.chat.id, "Попробуй еще раз")



#    markup = types.InlineKeyboardMarkup(row_width=3)
#    btn_1 = types.InlineKeyboardButton(text=questions["2"]["answer"]["1"], callback_data="btn21")
#    btn_2 = types.InlineKeyboardButton(text=questions["2"]["answer"]["2"], callback_data="btn22")
#    btn_3 = types.InlineKeyboardButton(text=questions["2"]["answer"]["3"], callback_data="btn23")
#    markup.add(btn_1, btn_2, btn_3)
#    bot.send_message(message.chat.id, questions["2"]["question"], reply_markup=markup)


if __name__=="__main__":
    bot.infinity_polling(none_stop=True)
