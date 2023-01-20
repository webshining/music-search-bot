from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import dp, _, bot
from app.states import Search
from app.keyboards import get_names_markup, get_music_markup
from utils import get_musics, get_text


@dp.message(Command('search'))
async def _search(message: Message, state: FSMContext):
    await message.answer(_("Enter song name:"))
    await state.set_state(Search.name)


@dp.message(Search.name)
async def _search_name(message: Message, state: FSMContext):
    names = await get_musics(message.text)
    if names:
        await state.clear()
        await message.answer(_("Select song:"), reply_markup=get_names_markup('search', names))
        await state.update_data(names=names)
    else:
        await message.answer(_("Song not found, enter correct name:"))


@dp.callback_query(lambda call: call.data.startswith('search'))
async def _search_callback(call: CallbackQuery):
    text = await get_text(call.data[7:])
    await call.message.edit_text(text, reply_markup=get_music_markup())


@dp.callback_query(lambda call: call.data.startswith('music'))
async def _music_callback(call: CallbackQuery, state: FSMContext):
    if call.data[6:] == 'back':
        data = await state.get_data()
        names = data.get('names')
        return await call.message.edit_text(_("Select song:"), reply_markup=get_names_markup('search', names))