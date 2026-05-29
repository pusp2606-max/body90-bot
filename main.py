from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

TOKEN = "СЮДА_ТВОЙ_ТОКЕН"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("💪 Моя программа"))
menu.add(KeyboardButton("🍎 Питание"))
menu.add(KeyboardButton("📈 Прогресс"))
menu.add(KeyboardButton("🔥 Мотивация"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = """
🔥 BODY90 BOT 🔥

Измени тело за 90 дней дома 💪

✅ Домашние тренировки
✅ Пресс
✅ V-shape
✅ Шире плечи
✅ Без зала
"""
    await message.answer(text, reply_markup=menu)

@dp.message_handler(lambda message: message.text == "💪 Моя программа")
async def workout(message: types.Message):
    text = """
🔥 ТРЕНИРОВКА ДНЯ

Отжимания:
4x15
⏱ Отдых 60 сек

Широкие отжимания:
4x12
⏱ Отдых 60 сек

Планка:
3x60 сек
⏱ Отдых 30 сек
"""
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "🍎 Питание")
async def food(message: types.Message):
    await message.answer("""
🍎 ПИТАНИЕ

🥚 Яйца
🍗 Курица
🥛 Творог
🍌 Бананы
💧 Вода 2л
""")

@dp.message_handler(lambda message: message.text == "📈 Прогресс")
async def progress(message: types.Message):
    await message.answer("""
📈 ПРОГРЕСС

🔥 Ты на пути к лучшему телу
💪 Главное — стабильность
""")

@dp.message_handler(lambda message: message.text == "🔥 Мотивация")
async def motivation(message: types.Message):
    await message.answer("""
🔥 МОТИВАЦИЯ

Не жди мотивацию.
Создай дисциплину ⚡
""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
