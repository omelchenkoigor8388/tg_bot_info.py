import telebot
from telebot import types

#парсер валют
from сurrencies import course_USD
from сurrencies import course_EUR
from сurrencies import course_RUB
from сurrencies import course_PLN
from сurrencies import course_GBP
from сurrencies import course_CHF
from сurrencies import course_BTC
from сurrencies import course_ETH
from сurrencies import course_BNB
from сurrencies import course_DOGE
from сurrencies import course_SHIB
from сurrencies import course_LTC

#парсер новин
from news import science_and_technology
from news import digital
from news import ukraine

#парсер погоди
from weather import weather_1
from weather import weather_2
from weather import weather_3
from weather import weather_4
from weather import weather_5
from weather import weather_6
from weather import weather_7
from weather import weather_8
from weather import weather_9
from weather import weather_10
from weather import weather_11
from weather import weather_12
from weather import weather_13
from weather import weather_14
from weather import weather_15
from weather import weather_16
from weather import weather_17
from weather import weather_18
from weather import weather_19
from weather import weather_20
from weather import weather_21
from weather import weather_22
from weather import weather_23
from weather import weather_24
from weather import weather_25

#інформація про бота
from info import text_info

TOREN = "5486552502:AAFLX5MbQ6jpA75sD0lEjHdsUeLtIPE5-UY"

bot = telebot.TeleBot(TOREN)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('📈Курс валют')
    item2 = types.KeyboardButton('🌎Новини')
    item3 = types.KeyboardButton('🌥Погода')
    item4 = types.KeyboardButton('📑Інформація про бота📑')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привіт, {0.first_name}!'.format(message.from_user), reply_markup = markup)

#----------------------------------------------------Меню валют------------------------------------------------------------------

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '📈Курс валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Валюти')
            item2 = types.KeyboardButton('Криптовалюти')
            item3 = types.KeyboardButton('⬅назад')
            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, '📈Курс валют', reply_markup = markup)

        elif message.text == 'Валюти':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Долар_USD')
            item2 = types.KeyboardButton('Євро_EUR')
            item3 = types.KeyboardButton('Рубль_RUB')
            item4 = types.KeyboardButton('Злотий_PLN')
            item5 = types.KeyboardButton('Фунта_GBP')
            item6 = types.KeyboardButton('Франк_CHF')
            item7 = types.KeyboardButton('⬅назад до меню валют')
            markup.add(item1, item2, item3, item4, item5, item6, item7)

            bot.send_message(message.chat.id, 'Валюти', reply_markup=markup)

        elif message.text == 'Криптовалюти':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Bitcoin')
            item2 = types.KeyboardButton('Ethereum')
            item3 = types.KeyboardButton('BNB')
            item4 = types.KeyboardButton('Dogecoin')
            item5 = types.KeyboardButton('Shiba Inu')
            item6 = types.KeyboardButton('Litecoin')
            item7 = types.KeyboardButton('⬅назад до меню валют')
            markup.add(item1, item2, item3, item4, item5, item6, item7)

            bot.send_message(message.chat.id, 'Криптовалюти', reply_markup=markup)

        elif message.text == 'Долар_USD':
            course_USD(message)
        elif message.text == 'Євро_EUR':
            course_EUR(message)
        elif message.text == 'Рубль_RUB':
            course_RUB(message)
        elif message.text == 'Злотий_PLN':
            course_PLN(message)
        elif message.text == 'Фунта_GBP':
            course_GBP(message)
        elif message.text == 'Франк_CHF':
            course_CHF(message)
        elif message.text == 'Bitcoin':
            course_BTC(message)
        elif message.text == 'Ethereum':
            course_ETH(message)
        elif message.text == 'BNB':
            course_BNB(message)
        elif message.text == 'Dogecoin':
            course_DOGE(message)
        elif message.text == 'Shiba Inu':
            course_SHIB(message)
        elif message.text == 'Litecoin':
            course_LTC(message)


# -----------------------------------------------Меню новин----------------------------------------------------------------

        elif message.text == '🌎Новини':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Наука и техника')
            item2 = types.KeyboardButton('Диджитал')
            item3 = types.KeyboardButton('Україна')
            item4 = types.KeyboardButton('⬅назад')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, '🌎Новини', reply_markup = markup)

        elif message.text == 'Наука и техника':
            science_and_technology(message)
        elif message.text == 'Диджитал':
            digital(message)
        elif message.text == 'Україна':
            ukraine(message)

# -----------------------------------------------Меню погоди----------------------------------------------------------------
        elif message.text == '🌥Погода':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Київська')
            item2 = types.KeyboardButton('Вінницька')
            item3 = types.KeyboardButton('Волинська')
            item4 = types.KeyboardButton('Дніпропетровська')
            item5 = types.KeyboardButton('Донецька')
            item6 = types.KeyboardButton('Житомирська')
            item7 = types.KeyboardButton('Закарпатська')
            item8 = types.KeyboardButton('Запорізька')
            item9 = types.KeyboardButton('Івано-Франківська')
            item10 = types.KeyboardButton('Кіровоградська')
            item11 = types.KeyboardButton('Луганська')
            item12 = types.KeyboardButton('Львівська')
            item13 = types.KeyboardButton('Миколаївська')
            item14 = types.KeyboardButton('Одеська')
            item15 = types.KeyboardButton('Полтавська')
            item16 = types.KeyboardButton('Рівненська')
            item17 = types.KeyboardButton('Сумська')
            item18 = types.KeyboardButton('Тернопільська')
            item19 = types.KeyboardButton('Харківська')
            item20 = types.KeyboardButton('Херсонська')
            item21 = types.KeyboardButton('Хмельницька')
            item22 = types.KeyboardButton('Черкаська')
            item23 = types.KeyboardButton('Чернівецька')
            item24 = types.KeyboardButton('Чернігівська')
            item25 = types.KeyboardButton('АР Крим')
            item26 = types.KeyboardButton('⬅назад')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
                      item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25,
                      item26)

            bot.send_message(message.chat.id, 'Оберіть область в якій бажаєте дізнатись рогоду', reply_markup=markup)

        elif message.text == 'АР Крим':
            weather_1(message)
        elif message.text == 'Вінницька':
            weather_2(message)
        elif message.text == 'Волинська':
            weather_3(message)
        elif message.text == 'Дніпропетровська':
            weather_4(message)
        elif message.text == 'Донецька':
            weather_5(message)
        elif message.text == 'Житомирська':
            weather_6(message)
        elif message.text == 'Закарпатська':
            weather_7(message)
        elif message.text == 'Запорізька':
            weather_8(message)
        elif message.text == 'Івано-Франківська':
            weather_9(message)
        elif message.text == 'Київська':
            weather_10(message)
        elif message.text == 'Кіровоградська':
            weather_11(message)
        elif message.text == 'Луганська':
            weather_12(message)
        elif message.text == 'Львівська':
            weather_13(message)
        elif message.text == 'Миколаївська':
            weather_14(message)
        elif message.text == 'Одеська':
            weather_15(message)
        elif message.text == 'Полтавська':
            weather_16(message)
        elif message.text == 'Рівненська':
            weather_17(message)
        elif message.text == 'Сумська':
            weather_18(message)
        elif message.text == 'Тернопільська':
            weather_19(message)
        elif message.text == 'Харківська':
            weather_20(message)
        elif message.text == 'Херсонська':
            weather_21(message)
        elif message.text == 'Хмельницька':
            weather_22(message)
        elif message.text == 'Черкаська':
            weather_23(message)
        elif message.text == 'Чернівецька':
            weather_24(message)
        elif message.text == 'Чернігівська':
            weather_25(message)
# -----------------------------------------------Функціонал кнопки інформації----------------------------------------------------------------

        elif message.text == '📑Інформація про бота📑':
            bot.send_message(message.chat.id, text_info)

#---------------------------------------------Функціонал кнопок назад-----------------------------------------------------------------

        elif message.text == '⬅назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('📈Курс валют')
            item2 = types.KeyboardButton('🌎Новини')
            item3 = types.KeyboardButton('🌥Погода')
            item4 = types.KeyboardButton('📑Інформація про бота📑')

            markup.add(item1, item2, item3,item4)

            bot.send_message(message.chat.id, '⬅назад', reply_markup = markup)

        elif message.text == '⬅назад до меню валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Валюти')
            item2 = types.KeyboardButton('Криптовалюти')
            item3 = types.KeyboardButton('⬅назад')
            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, '📈Курс валют', reply_markup=markup)

bot.polling(none_stop = True)
