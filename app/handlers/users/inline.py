import uuid
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.fsm.context import FSMContext

from loader import dp, _
from utils import get_names
from app.keyboards import get_names_markup


@dp.inline_query()
async def _inline(query: InlineQuery, state: FSMContext):
    text = query.query or ""
    names = get_names(text)
    await state.update_data(name=text)
    item = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title="Search",
        input_message_content=InputTextMessageContent(message_text=text) if names else InputTextMessageContent(message_text=_("Song not found")),
        reply_markup=get_names_markup('search', names) if names else None
    )
    await query.answer(results=[item], cache_time=1)