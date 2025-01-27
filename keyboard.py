


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_keyboard():
    # Создаем клавиатуру и сразу добавляем кнопки
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ])
    return keyboard

#--------------------------

def get_links_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Видео", url='https://yandex.ru/search/?text=видео&lr=11418&clid=3762826-0&win=659&src=suggest_B')],
        [InlineKeyboardButton(text="Новости", url='https://yandex.ru/search/?text=новости&lr=11418&clid=3762826-0&win=659&src=suggest_B')],
        [InlineKeyboardButton(text="Музыка", url='https://yandex.ru/search/?text=музыка&lr=11418&clid=3762826-0&win=659&src=suggest_B')]
])
    return keyboard

#---------------------------

def get_dynamic_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
        ])
    return keyboard




def get_extended_dynamic_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
    [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
        ])
    return keyboard