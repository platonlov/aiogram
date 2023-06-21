from aiogram import Bot, executor, Dispatcher, types
from config import api_token

bot = Bot(token= api_token)
b = Dispatcher(bot)
help = """
/help - список команд
/start - начать работу с ботом
/hi - поздороваться
"""
@b.message_handler(commands=['help'])
async def help_comment(msg: types.Message):
    await msg.reply(text=help)

@b.message_handler(commands=['start'])
async def help_comment(msg: types.Message):
    await msg.answer(text="стартуем!")
    await msg.delete()


@b.message_handler(commands=['hi'])
async def help_comment(msg: types.Message):
    await msg.reply(text="привет")


if __name__ == '__main__':
    executor.start_polling(b)