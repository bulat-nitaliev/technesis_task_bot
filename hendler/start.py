from aiogram import  types, F
from aiogram.filters import CommandStart
from aiogram import Router
from keyboard.keyboards import  starts
from aiogram import Bot
from decouple import config
import pandas as pd
from repository import get_repo

bot = Bot(token=config('TOKEN'))

        
        
router = Router()

@router.message(F.text=='Добавить файл')
async def start_(message:types.Message):
    await message.answer(
        "Пожалуйста, прикрепите ваш Excel-файл.", 
        reply_markup=types.ReplyKeyboardRemove()
        )


@router.message(F.content_type.in_([types.ContentType.DOCUMENT]))
async def handle_document(message: types.Message):
    document: types.Document = message.document
    file_name = document.file_name

    if file_name.lower().endswith((".xlsx", ".xls")):
        await document.bot.download(document.file_id, file_name)
      
        res = pd.read_excel(file_name)
        lst_sites = res.to_dict(orient='records')
        get_repo().add_sites(lst_sites)      
        await message.answer(f"Файл {file_name} успешно получен!  \n{res}")
    else:
        await message.answer("Этот тип файла не поддерживается. Пожалуйста, отправьте Excel-файл.")


@router.message(CommandStart)
async def start_bot(message:types.Message):
    await message.answer('''
        Здравствуйте! 👋\n\n
        Этот бот который по переданному файлу excel ,\n
        парсит указанный сайт и товар сохраняя цену,\n
        
        Необходимо  прожать кнопку "Добавить файл"
        \n\n
        👇''' , reply_markup=starts)
