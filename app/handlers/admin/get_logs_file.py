from aiogram.types import Message, InputFile
from aiogram.dispatcher.filters import Command
from loader import dp
from pathlib import Path


@dp.message_handler(Command('get_logs'))
async def get_logs_file_handler(message: Message):
    file_path = f'{Path(__file__).absolute().parent.parent.parent.parent}/data/logs/log.out'
    await message.answer_document(document=InputFile(file_path))
