import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu

from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):


    await message.answer(
        "Xush kelibsiz! Do'konimizdagi mahsulotlarni ko'rish uchun quyidagi Menu tugmasini bosing",
        reply_markup=menu,
    )

    # ADMINGA xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
