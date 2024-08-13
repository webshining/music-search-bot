import pickle

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.handlers.users.search import get_song_state
from app.keyboards import SongCallback, get_songs_markup, get_song_markup, SongsCallback
from database.models import Song, User
from loader import dp, _


@dp.callback_query(SongsCallback.filter())
async def select_song_(call: CallbackQuery, state: FSMContext, callback_data: SongsCallback, user: User):
    song = await get_song_state(callback_data.id, state)

    if song.text:
        library = song.id in [s.id for s in user.songs]
        text = song.get_text(chords=False)
        markup = get_song_markup(callback_data.data, song.id, library=library)
        return await call.message.edit_text(text, reply_markup=markup)
    return await call.answer(_("Looks like the song has no lyrics"), show_alert=True)


@dp.callback_query(SongCallback.filter((F.data == "search") & (F.action == "back")))
async def back_to_result_(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    songs = data.get("songs")
    songs = pickle.loads(bytes.fromhex(songs)) if songs else []

    if songs:
        text = _("Select song:") + "\n"
        for i, s in enumerate(songs):
            text += f"\n<b>{i + 1}.</b> <u>{s.name}</u> - {s.artist}"
        return await call.message.edit_text(text, reply_markup=get_songs_markup("search", songs))
    return await call.message.edit_text(_("Looks like the songs are out of memory or you used /cancel"),
                                        reply_markup=None)


@dp.callback_query(SongCallback.filter(F.action.startswith("chords")))
async def song_chords_(call: CallbackQuery, state: FSMContext, callback_data: SongCallback, user: User):
    song = await get_song_state(callback_data.id, state)

    chords = eval(callback_data.action[7:])
    library = song.id in [s.id for s in user.songs]

    return await call.message.edit_text(song.get_text(chords),
                                        reply_markup=get_song_markup(callback_data.data, song.id, chords=chords,
                                                                     library=library))


@dp.callback_query(SongCallback.filter(F.action == "music"))
async def song_music_(call: CallbackQuery, state: FSMContext, callback_data: SongCallback):
    song = await get_song_state(callback_data.id, state)

    if song.file:
        return await call.message.answer_audio(audio=song.file)
    return await call.answer(_("Looks like there’s no music on the resource for this song"), show_alert=True)


@dp.callback_query(SongCallback.filter(F.action.startswith("library")))
async def song_library_(call: CallbackQuery, state: FSMContext, callback_data: SongCallback, user: User):
    song = await get_song_state(callback_data.id, state)

    chords = eval(SongCallback.unpack(call.message.reply_markup.inline_keyboard[0][0].callback_data).action[7:])
    library = eval(callback_data.action[8:])
    if library:
        songs = [*user.songs, Song(id=song.id, name=song.name, artist=song.artist)]
    else:
        songs = list(filter(lambda s: s.id != song.id, user.songs))
    await user.update(id=user.id, songs=[s.model_dump() for s in songs])

    return await call.message.edit_reply_markup(
        reply_markup=get_song_markup(callback_data.data, song.id, chords=not chords, library=library))
