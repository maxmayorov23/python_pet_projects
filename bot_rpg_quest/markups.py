from telebot import types
import data

def create_list_of_commands(bot, chat_id):
    """
    Создание команд для бота
    """
    c1 = types.BotCommand(command='start', description='Старт')
    c2 = types.BotCommand(command='help', description='Как работает бот?')
    c3 = types.BotCommand(command='contacts', description='Контакты')
    bot.set_my_commands([c1, c2, c3])
    bot.set_chat_menu_button(chat_id, types.MenuButtonCommands('commands'))


def create_main_menu():
    """
    Создание главного меню игры
    :return: markup
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btns = []
    for val in data.buttons["main"].values():
        btns.append(types.KeyboardButton(val))
    markup.add(*btns)

    return markup


def create_btns(data: dict) -> list:

    markup = types.InlineKeyboardMarkup(row_width=1)

    btns = []
    for key, val in data.items():
        key = "✔ " + key
        btns.append(types.InlineKeyboardButton(text=key, callback_data=val))
    markup.add(*btns)

    return markup