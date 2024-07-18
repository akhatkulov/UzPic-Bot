from aiogram import types
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from keyboards.inline.action_pic import act_pic

from utils.photo import photo_link
from utils.rbg import remove_background

x = {}


@dp.message_handler(content_type=['photo'])
async def bot_echo(message: types.Message,state: FSMContext):
    x[str(message.chat.id)]=message.photo
    await message.reply("Rasmingiz qabul qilindi, amalni tanlang",reply_markup= await act_pic())

@dp.callback_query_handler(text="remove_bg")
async def rm_bg(call: types.CallbackQuery):
    y = await remove_background(x[str(call.message.chat.id)])
    await bot.send_photo(chat_id=call.message.chat.id,photo=y)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="put_host")
async def put_host(call: types.CallbackQuery):
    y = await put_host(x[str(call.message.chat.id)])
    await bot.send_message(chat_id=call.message.chat.id,text=y)
    await call.answer(cache_time=60)