from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

button_1 = types.InlineKeyboardButton("Биология", callback_data='biology')
button_2 = types.InlineKeyboardButton("География", callback_data='geography')
button_3 = types.InlineKeyboardButton("Математика", callback_data='math')
button_4 = types.InlineKeyboardButton("Физика", callback_data='physics')
button_5 = types.InlineKeyboardButton("Английский", callback_data='english')
button_6 = types.InlineKeyboardButton("Украинский язык", callback_data='ukraine_language')
button = types.InlineKeyboardMarkup().add(button_1, button_2, button_3, button_4, button_5, button_6)

english_1 = types.InlineKeyboardButton("Словарь", callback_data='words')
english_2 = types.InlineKeyboardButton("Конспект", callback_data='engl')
english = types.InlineKeyboardMarkup().add(english_1, english_2)


