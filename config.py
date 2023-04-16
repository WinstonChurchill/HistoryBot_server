from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,\
                          InlineKeyboardMarkup, InlineKeyboardButton

Keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_standart1 = KeyboardButton('/start')
button_standart2 = KeyboardButton('/help')
button_standart3 = KeyboardButton('/play')
button_standart4 = KeyboardButton('/state')
button_standart5 = KeyboardButton('/seed')
Keyboard.add(button_standart1).add(button_standart2).add(button_standart3).add(button_standart4).add(button_standart5)

Keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_standart11 = KeyboardButton('Назад')
button_standart22 = KeyboardButton('Пропустить')
button_standart33 = KeyboardButton('Что такое сид?')
Keyboard1.add(button_standart11).add(button_standart22).add(button_standart33)

token = '5716542126:AAHeoVYBJHNZjPipwt6i50Fmwl57bdF-K38'

txt_seed = """Seed - ключ генерации опроса

1.1.1.1 - пример

Seed это числы отделенные . есть 4 части seed 
I часть сида отвечает за формат вопроса. Спрашивают дату или событие. Может быть 1 или 2 
II часть сида отвечает за наличие вопросов во временном периорды. Всего есть 7 временных периордов: 860-988 года, 1000-1499 года, 1500-1699 года, 18 век, 19 век, 20 век, 21 век. Цифра в сиде 1 отвечает за нахождение всех периордов. Дальше цифра 2 в сиде отвечает за первый периорд, цифра 3 в сиде отвечает за второй периорд и т д 
III часть сида отвечает за количество вопросов от 1-100 штук. В рандомном генераторе сида от 5-30 вопросов 
IV часть сида отвечает за генерацию вопросов

При введение текста он преобразуется в числовой seed. Например a преобразуется в 2.4.17.611655"""

txt_hello = """Привет я History Bot и помогу тебе подготовится к ОГЭ/ЕГЭ по истории!
Если нужна помощь, напиши /help
Если хочешь узнать статистику /state
Если хочешь пройти опрос /play [seed]
Если хочешь узнать про seed, то /seed"""

txt_help = """У тебя возникла проблема?
Напиши /play [seed] для того чтобы пройти опрос
Напиши /state для того чтобы узнать свою статистику

Seed - ключ генерации опроса

1.1.1.1 - пример

Seed это числы отделенные . есть 4 части seed 
I часть сида отвечает за формат вопроса. Спрашивают дату или событие. Может быть 1 или 2 
II часть сида отвечает за наличие вопросов во временном периорды. Всего есть 7 временных периордов: 860-988 года, 1000-1499 года, 1500-1699 года, 18 век, 19 век, 20 век, 21 век. Цифра в сиде 1 отвечает за нахождение всех периордов. Дальше цифра 2 в сиде отвечает за первый периорд, цифра 3 в сиде отвечает за второй периорд и т д 
III часть сида отвечает за количество вопросов от 1-100 штук. В рандомном генераторе сида от 5-30 вопросов 
IV часть сида отвечает за генерацию вопросов

При введение текста он преобразуется в числовой seed. Например a преобразуется в 2.4.17.611655"""

errors = (
    '1: Unknown error',
    '2: No admin rights',
    '101: file not found',
    '102: file connection error',
    '201: question creation error',
    '202: error this in not seed',
    '202: loading error',
    '301: error create prof',
    '302: error create prof file',
    '/log: logging file',
    '/start: creating a profile and displaying information',
    '/datad: return data dates',
    '/datap: return data people',
    '/admin: on/off admin',
    '/help: info',
    '/play: testing',
    '/period: return period',
    '/clear: clear cash profile',
    '/state: static prodile'
)

def static_txt(state):
    return f"""Дата регистрации: {state[0]}
Количество пройденных опросов: {state[1]}
Количество отвеченных вопросов: {state[2]}
Количество правильных ответов: {state[3]}
Количество неправильных ответов: {state[4]}
    """