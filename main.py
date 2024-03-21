"""Dasturchi @pragrammer_uz"""

import logging
from aiogram import Dispatcher, Bot, types
from Tarjima import to_cyrillic, to_latin
from tokken import bot
import asyncio
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot, parse_mode='HTML')

dp = Dispatcher()

@dp.message(Command('start'))
async def boshlash(message: types.Message):
    odi = message.from_user.first_name
    await message.answer(f"<b>Assalomu alaykum👋 {odi}\n\n- Men sizga Lotin tilida yozilgan yozuvlarni krill tiliga krill ni esa lotinga o'zgartirishda yordam beraman. 🤖\n\n🫡 Shunchaki kerakli matnni menga yuboring. 👉📝</b>")


@dp.message()
async def latin(message: types.Message):
    text = message.text

    if text.isascii():
        kril = to_cyrillic(text)
        await message.reply(f"📋Матн устига босиб авто нусха қилиб олишингиз мумкин\n\n<code>{kril}</code>")
    else:
        lotincha = to_latin(text)
        await message.reply(f"📋Matn ustiga bosib avto nusxa qilib olishingiz mumkin\n\n<code>{lotincha}</code>")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot ish faolyatini tugatdi!")
