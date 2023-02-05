# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.utils.markdown import hcode
# from bot import Bot, Dispatcher
import time
from aiogram import types
from aiogram.types import CallbackQuery
from tgbot.keyboards.inline import main_keyboard
from bot import bot, dp
from tgbot.config import admin_id
from zoneinfo import ZoneInfo
from datetime import datetime


async def send_to_admin(dp):
    " Функція відправки повідомлення адміну"
    await bot.send_message(chat_id=admin_id, text="Бот активований")
    await bot.send_message(chat_id=admin_id, text="Натисніть   /start")


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_full_name = message.from_user.full_name
    timestamp_now = datetime.now()

    insert_query = (f"INSERT INTO message (message, userid, message_time) "
                    f"VALUES ({message.text}, {message.from_user['id']}, {timestamp_now})")
    await bot.send_message(user_id, text="Вітаю, я телеграм бот")
    time.sleep(2)
    await bot.send_message(user_id,
                           text=f"user_id: {user_id}\n"
                                f"first_name: {first_name}\n"
                                f"last_name: {last_name}\n"
                                f"user_full_name: {user_full_name}\n"
                                f"time: {timestamp_now}")


@dp.message_handler()
async def any_massage_handler(message: types.Message):
    user_id = message.from_user.id
    data = datetime.now()
    await bot.send_message(user_id, text=f"Прошу відмітити свою присутність на уроці {data}",
                           reply_markup=main_keyboard)

#
#
# async def bot_echo(message: types.Message):
#     text = [
#         "Эхо без состояния.",
#         "Сообщение:",
#         message.text
#     ]
#
#     await message.answer('\n'.join(text))
#
#
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state_name = await state.get_state()
#     text = [
#         f'Эхо в состоянии {hcode(state_name)}',
#         'Содержание сообщения:',
#         hcode(message.text)
#     ]
#     await message.answer('\n'.join(text))
#
#
# def register_echo(dp: Dispatcher):
#     dp.register_message_handler(bot_echo)
#     dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
