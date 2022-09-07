from aiogram.types import Message, InputFile
from aiogram.dispatcher.filters import Command
from loader import dp
from pathlib import Path


@dp.message_handler(Command('get_database'))
async def get_db_file_handler(message: Message):
    file_path = f'{Path(__file__).absolute().parent.parent.parent.parent}/data/database.sqlite'
    await message.answer_document(document=InputFile(file_path))
