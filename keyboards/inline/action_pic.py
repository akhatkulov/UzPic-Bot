from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButon

async def act_pic():
    x = InlineKeyboardMarkup(width=1)
    btn1 = InlineKeyboardButon(text="Orqa fonni o'chirish",callback_data="remove_bg")
    btn2 = InlineKeyboardButon(text="Xostingga joylash",callback_data="put_host")
    x.add(btn1,btn2)
    return x