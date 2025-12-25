import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "8243386470:AAFcokjpSw2PRhfGrqi3dTjw_gOElBBdMnY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "📈 Курс валют\n"
        "Открой график:\n"
        "http://127.0.0.1:5000"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
