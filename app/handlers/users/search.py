from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import dp, _, bot
from app.states import Search
from app.keyboards import get_names_markup, get_back_markup
from utils import get_names, get_text


@dp.message(Command('search'))
async def _search(message: Message, state: FSMContext):
    await message.answer(_("Enter song name:"))
    await state.set_state(Search.name)


@dp.message(Search.name)
async def _search_name(message: Message, state: FSMContext):
    names = get_names(message.text)
    if names:
        await state.clear()
        await message.answer(_("Select song:"), reply_markup=get_names_markup('search', names))
        await state.update_data(name=message.text)
    else:
        await message.answer(_("Song not found, enter correct name:"))
    

@dp.callback_query(Text(startswith='search'))
async def _search_callback(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data[7:] == 'back':
        data = await state.get_data()
        names = get_names(data.get('name'))
        if names:
            if call.inline_message_id:
                await bot.edit_message_text(text=_("Select song:"), inline_message_id=call.inline_message_id, reply_markup=get_names_markup('search', names))
            else:
                await call.message.edit_text(text=_("Select song:"), reply_markup=get_names_markup('search', names))
        else:
            if call.inline_message_id:
                await bot.edit_message_text(text=_("Song not found"), inline_message_id=call.inline_message_id, reply_markup=None)
            else:
                await call.message.edit_text(text=_("Song not found"), reply_markup=None)
    else:
        text = get_text(call.data[7:])
        if call.inline_message_id:
            await bot.edit_message_text(text=text, inline_message_id=call.inline_message_id, reply_markup=None)
        else:
            await call.message.edit_text(text=text, reply_markup=get_back_markup('search'))
