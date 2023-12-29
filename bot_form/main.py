'''
Телеграм бот: Анкета (Quiz) пользователя

В данном "квизе" будут проверяться базовые знания физики 7 класса
'''

import telebot
from telebot import types
import data

API_TOKEN = '6408579321:AAFCNEkjbsIydN-hbncO_GJw3CSTIs9fmxU'

bot = telebot.TeleBot(API_TOKEN)

questions = data.questions
help_text = data.help_text
welcome_text = data.welcome_text
congratulations_text = data.congratulations_text
correct_answers = data.correct_answers

#хранение данных о пользователях
user_data = {}

def init_user_data(message, step = 1):
    '''
    Функция для установки данных пользователя
    :param message: объект телеграм API
    :param step: шаг для меню
    '''
    user_data[message.chat.id] = {
        "first_name": message.from_user.first_name,
        "step": 1,
        "result": 0
    }

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}. {welcome_text}")
    init_user_data(message)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, help_text )

@bot.message_handler(commands=['test'])
def send_welcome(message):

    if not user_data.get(message.chat.id):
        init_user_data(message)

    step = user_data[message.chat.id].get("step")
    send_task(message, step)


def create_menu(data):
    '''
    Создание маркапа кнопок
    '''
    markup = types.InlineKeyboardMarkup(row_width=1)
    btns_list = []
    for val in data.values():
        btns_list.append(types.InlineKeyboardButton(val, callback_data=val))

    markup.add(*btns_list)

    return markup

def send_task(message, step):

    # создание меню
    markup = create_menu(questions[step].get("answer"))

    # Отправка сообщения с вопросом и кнопками
    question = questions[step].get("question")
    bot.send_message(message.chat.id, question, reply_markup=markup)

def finish(message):

    points = user_data[message.chat.id]["result"]

    if points == 3:
        bot.send_message(message.chat.id, congratulations_text)
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так")

# Обработка результатов теста
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    correct_answer = correct_answers[call.message.text]
    # print(correct_answer)

    if call.data == correct_answer:
        bot.send_message(call.message.chat.id, "Это правильный ответ")

        # +1 бал за правильный ответ
        user_data[call.message.chat.id]["result"] += 1

        # проверка текущего шага
        step = user_data[call.message.chat.id].get("step")
        if step < len(questions):
            user_data[call.message.chat.id]["step"] += 1
            send_task(call.message, user_data[call.message.chat.id]["step"])
        else:
            finish(call.message)

    else:
        bot.send_message(call.message.chat.id, "Попробуй еще раз")


if __name__=="__main__":
    bot.infinity_polling(none_stop=True)
