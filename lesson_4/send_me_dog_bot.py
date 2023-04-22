import os

import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

TOKEN_API = os.getenv('TOKEN')

HELP_COMMAND = """
/help - command list
/start - bot start
/description - bot description
"""

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('🐶send me dog!🐶'))


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(
        text='Welcome! Shall I send you a doggie?',
        reply_markup=kb,
    )
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await message.answer(
        'This bot knows how to send photos/videos of cute dogs🐕'
    )
    await message.delete()


@dp.message_handler()
async def send_dog_media(message: types.Message):
    media_url = requests.get('https://random.dog/woof.json').json().get('url')
    if media_url.lower().endswith(('jpg', 'jpeg', 'png')):
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=media_url
        )
    elif media_url.lower().endswith(('mp4', 'gif')):
        await bot.send_video(
            chat_id=message.from_user.id,
            video=media_url
        )
    else:
        await message.answer(text='oops! something went wrong... try again🐕')
    await message.delete()


async def on_startup(_):
    print('Bot successfully started')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
