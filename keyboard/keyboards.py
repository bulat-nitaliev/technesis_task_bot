from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



starts = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Добавить файл"),
                ]
            ],
            resize_keyboard=True,
            input_field_placeholder='Добавить файл'
        )


