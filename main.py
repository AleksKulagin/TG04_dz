import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery
from keyboard import get_main_menu_keyboard, get_links_keyboard, get_dynamic_keyboard, get_extended_dynamic_keyboard

# Указываем токен вашего бота
API_TOKEN = ''

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Выберите действие:", reply_markup=get_main_menu_keyboard())


@dp.message(Command('help'))
async def  help(messages: Message):
    await messages.answer(f'Еще текст по команде help {messages.from_user.first_name}')



async def handle_text(message: Message):
    if message.text == "Привет":
        await message.answer(f"Здравтствуйте, {message.from_user.full_name}!")
    elif message.text == "Пока":
        await message.answer(f"До свидания, {message.from_user.full_name}!")
#--------------------------------------------------------------------------------------


# Задание 2: Кнопки с URL-ссылками
async def send_links(message: Message):
    await message.answer("Вот ссылки на полезные ресурсы:", reply_markup=get_links_keyboard())

#----------------------------------------------------------------------------------------

# Задание 3: Динамическое изменение клавиатуры
async def dynamic_keyboard(message: Message):
    await message.answer("Нажмите кнопку ниже:", reply_markup=get_dynamic_keyboard())

async def handle_callback_query(callback_query: CallbackQuery):
    if callback_query.data == "show_more":
        await callback_query.message.edit_reply_markup(reply_markup=get_extended_dynamic_keyboard())
    elif callback_query.data == "option_1":
        await callback_query.answer()
        await callback_query.message.answer("Вы выбрали Опцию 1.")
    elif callback_query.data == "option_2":
        await callback_query.answer()
        await callback_query.message.answer("Вы выбрали Опцию 2.")

async def main():
    # Регистрация обработчиков
    dp.message.register(start, Command("start"))
    dp.message.register(send_links, Command("links"))
    dp.message.register(dynamic_keyboard, Command("dynamic"))
    dp.message.register(handle_text, F.text)
    dp.callback_query.register(handle_callback_query)
    await dp.start_polling(bot)

    # Запуск бота
    asyncio.run(dp.start_polling(bot))

if __name__ == "__main__":
    asyncio.run(main())
