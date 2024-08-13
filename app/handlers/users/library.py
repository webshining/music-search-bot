from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.keyboards import get_songs_markup, SongCallback
from database.models import User
from loader import dp, _


@dp.message(Command("library"))
async def library_(message: Message, user: User):
    text = _("Select song:") + "\n"
    for i, s in enumerate(user.songs):
        text += f"\n<b>{i + 1}.</b> <u>{s.name}</u> - {s.artist}"

    await message.answer(text, reply_markup=get_songs_markup("library", user.songs))


@dp.callback_query(SongCallback.filter((F.data == "library") & (F.action == "back")))
async def back_to_library_(call: CallbackQuery, user: User):
    text = _("Select song:") + "\n"
    for i, s in enumerate(user.songs):
        text += f"\n<b>{i + 1}.</b> <u>{s.name}</u> - {s.artist}"
    await call.message.edit_text(text, reply_markup=get_songs_markup("library", user.songs))
