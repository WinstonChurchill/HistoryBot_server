import logging
import json
import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import filters

from config import *
from BasPep import DataPeople, FilePeop
from BasDat import BasaDate
from vopros import vopros

logging.basicConfig(level=logging.INFO, filename="botlog.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

bot = Bot(token)
dp = Dispatcher(bot)

DataBaz = DataPeople()
BasaDates = BasaDate()

logging.info("inclusion")


#Комманды админа
@dp.message_handler(commands=['admin'])
async def process_admin_command(message: types.Message):
    logging.info(f"Command: admin, id:{message.from_user.id}")
    DataBaz.admin_redit(str(message.from_user.id))
    await bot.send_message(message.from_user.id, DataBaz.return_data()[str(message.from_user.id)]['admin'])

@dp.message_handler(commands=['log'])
async def process_log_command(message: types.Message):
    if DataBaz.admin_prov(str(message.from_user.id)):
        logging.info(f"Command: log, id:{message.from_user.id}")
        await message.reply_document(open('botlog.log', 'rb'))
    else:
        await bot.send_message(message.from_user.id, 'Error 2')

@dp.message_handler(commands=['datad'])
async def process_datad_command(message: types.Message):
    if DataBaz.admin_prov(str(message.from_user.id)):
        logging.info(f"Command: datad, id:{message.from_user.id}") 
        await message.reply_document(open('files/basedate.json', 'rb'))
    else:
        await bot.send_message(message.from_user.id, 'Error 2')

@dp.message_handler(commands=['datap'])
async def process_dataз_command(message: types.Message):
    if DataBaz.admin_prov(str(message.from_user.id)):
        logging.info(f"Command: datap, id:{message.from_user.id}")
        await message.reply_document(open('files/datapeople.json', 'rb'))
    else:
        await bot.send_message(message.from_user.id, 'Error 2')

@dp.message_handler(commands=['period'])
async def process_period_command(message: types.Message):
    if DataBaz.admin_prov(str(message.from_user.id)):
        logging.info(f"Command: datap, id:{message.from_user.id}")
        await bot.send_message(message.from_user.id, BasaDates.return_period())
    else:
        await bot.send_message(message.from_user.id, 'Error 2')

@dp.message_handler(commands=['clear'])
async def process_clear_command(message: types.Message):
    DataBaz.new_file(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Cash clear!')


#Обычные комманды
@dp.message_handler(commands=['state'])
async def process_state_command(message: types.Message):
    logging.info(f"Command: state, id:{message.from_user.id}")
    if DataBaz.file_prov(message.from_user.id) == 0:
        DataBaz.new_file(message.from_user.id)
    filesworks = FilePeop(message.from_user.id)
    txt = static_txt(filesworks.state())
    await bot.send_message(message.from_user.id, txt, reply_markup=Keyboard)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    logging.info(f"Command: help, id:{message.from_user.id}")
    if DataBaz.admin_prov(message.from_user.id):
        await message.reply('\n'.join(errors), reply_markup=Keyboard)
    else:
        await message.reply(txt_help, reply_markup=Keyboard)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    logging.info(f"Command: start, id:{message.from_user.id}")
    if DataBaz.proverka_in(str(message.from_user.id)) == 0:
        logging.info(f'creat prof. id: {message.from_user.id}')
        DataBaz.new_data(str(message.from_user.id))
    await message.reply(txt_hello, reply_markup=Keyboard)
    await message.reply_photo(open('files/cash.jpg', 'rb'))

@dp.message_handler(commands=['seed'])
async def process_seed_command(message: types.Message):
    logging.info(f"Command: seed, id:{message.from_user.id}")
    await message.reply(txt_seed)

@dp.message_handler(commands=['play'])
async def process_play_command(message: types.Message):
    logging.info(f"Command: play, id:{message.from_user.id}")
    if DataBaz.file_prov(message.from_user.id) == 0:
        DataBaz.new_file(message.from_user.id)
    fileswork = FilePeop(message.from_user.id)
    work = message.text.split('/play ')
    if work[0] == '/play':
        seed = 0
    else:
        seed = work[1]
    vopross = vopros(BasaDates.return_basa_date(), seed)
    now = datetime.datetime.now()
    fileswork.new_quast(seed, now.strftime("%d/%H/%M/%S"), len(list(vopross)))
    await message.reply(vopross, reply_markup=types.ReplyKeyboardRemove())


#Обработчик сообщений
@dp.message_handler()
async def echo_message(msg: types.Message):
    logging.info(f"Message:{msg.text}, id: {msg.from_user.id}")
    await bot.send_message(msg.from_user.id, 'Я не знаю как ответить попробуй /help')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)