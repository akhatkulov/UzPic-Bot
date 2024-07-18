from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n<b>Ushbu bot rasmlar bilan ishlashda sizga juda qo'l keladi. Ushbu bot nima qila oladi?</b>\n\n1.Rasmlarni hostingga joylab sizga uning linki beradi.\n2.Rasmning orqa fonini olib tashlaydi\n\n<b>Imkoniyatlardan foydalanish uchun shunchaki rasmni yuboring)</b>",parse_mode="html")
