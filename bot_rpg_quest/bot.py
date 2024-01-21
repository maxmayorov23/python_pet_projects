'''
Бот RPG-квест "Красная Сеть: За Гранью Марсианских Вершин"

Сюжет создан с помощью нейросетей.

Максим Майоров
https://github.com/maxmayorov23
'''

import telebot
from telebot import types
import time
import json
import os
from dotenv import load_dotenv
import markups as nav # menu
import data # text information

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# Описание локаций игры
json_file_path = 'data.json'
with open(json_file_path, 'r') as file:
    data_location = json.load(file)

# Хранение данных о пользователях
user_data = {}  

def init_user_data(message):
    '''
    Установка данных о пользователе
    '''
    user_data[message.chat.id] = {
        "first_name" : message.from_user.first_name,
    }
    print(user_data)

# Handle '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, data.help_text)

# Handle '/contacts'
@bot.message_handler(commands=['contacts'])
def send_welcome(message):
    bot.reply_to(message, data.contact_text)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):

    # Создание словаря с данными пользователя
    init_user_data(message)

    # Создание команд бота
    nav.create_list_of_commands(bot, message.chat.id)

    # Приветствие пользователя
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! {data.welcome_text}")
    
    # Цель игры
    time.sleep(3)
    bot.send_message(message.chat.id, data.intro_text)
    
    # Ролик о сюжете
    time.sleep(4)
    bot.send_message(message.chat.id, data.intro_text2)
    time.sleep(2)
    with open('media/information_promo.mp4', 'rb') as f:
      bot.send_video(message.chat.id, f)
    
    # Отправка кнопки старта игры
    time.sleep(10)
    markup = nav.create_main_menu()
    bot.send_message(message.chat.id, "<b>Можешь посмотреть полный клип игры. A eсли хочешь уже начать игру, жми Game!</b>", parse_mode="HTML", reply_markup=markup)


# Обработка кнопок главного меню
@bot.message_handler(content_types=['text'])
def start_game(message):

  if (message.chat.type == "private"): 
    # Начало игры
    if ("Game" in message.text): 
      markup = nav.create_btns(data_location.get("start",{}).get("options", None))

      with open(data_location.get("start",{}).get("image", None), 'rb') as f:
        bot.send_message(message.chat.id, data_location.get("start",{}).get("description", None))
        bot.send_photo(message.chat.id, f) 
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)
    # Отправки клипа
    if ("клип" in message.text): 
        # Промо ролик
        with open('media/video_clip.mp4', 'rb') as f:
          bot.send_video(message.chat.id, f)





# Обработка ответов в игре
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  '''
  Обработка inline-кнопок
  '''

  if call.data == data.victory_code:
    finish(call.message)
  else:
    # Имя локации на кнопке
    next_location = call.data
    # Отправка вопроса по выбранной локации
    send_question(call.message, next_location)


def send_question(message, next_location):
  '''
  Отправка следующего вопроса пользователю.
  '''
  markup = nav.create_btns(data_location.get(next_location, {}).get("options", None))

  with open(data_location[next_location]["image"], 'rb') as f:
    bot.send_photo(message.chat.id, f) 
    question = data_location.get(next_location, {}).get("description", None)
    bot.send_message(message.chat.id, question, reply_markup=markup)

def finish(message):
  bot.send_message(message.chat.id, data.congratulations_text)
  with open("media/10.png", 'rb') as f:
    bot.send_photo(message.chat.id, f) 
  # Аудио
  time.sleep(5)
  with open('media/marsian_misteria.mp3', 'rb') as f:
    bot.send_audio(message.chat.id, f)

if __name__=="__main__":
    bot.infinity_polling(none_stop=True)



