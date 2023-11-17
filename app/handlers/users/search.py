from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards import get_song_markup, get_songs_markup
from app.states import Search
from loader import _, dp
from utils import get_songs, get_text


@dp.message(Command('search'))
async def search_(message: Message, state: FSMContext):
    await message.answer(_("Enter song name:"))
    await state.set_state(Search.name)


@dp.message(Search.name)
async def search_name_(message: Message, state: FSMContext):
    songs = await get_songs(message.text)
    if songs:
        await message.answer("Select song:", reply_markup=get_songs_markup('search', songs))
        await state.clear()
        await state.update_data(songs=songs)
    else:
        await message.answer("Song with this name was not found, please enter another name:")


@dp.callback_query(lambda call: call.data.startswith('search'))
async def search_callback_(call: CallbackQuery):
    text = await get_text(call.data[7:])
    await call.message.edit_text(text, reply_markup=get_song_markup())


@dp.callback_query(lambda call: call.data.startswith('song'))
async def song_callback_(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data[5:] == 'back':
        songs = data.get('songs')
        if songs:
            await call.message.edit_text("Select song:", reply_markup=get_songs_markup('search', songs))
        else:
            await call.message.edit_text(_("It looks like there is no songs in memory or you wrote /cancel"), reply_markup=None)
            await state.clear()
    