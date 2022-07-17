import telebot
import requests
from bs4 import BeautifulSoup as BS

TOREN = "5486552502:AAFLX5MbQ6jpA75sD0lEjHdsUeLtIPE5-UY"

bot = telebot.TeleBot(TOREN)

def weather_1(message):
    r = requests.get('https://ua.sinoptik.ua/погода-крим')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_2(message):
    r = requests.get('https://ua.sinoptik.ua/погода-вінниця')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_3(message):
    r = requests.get('https://ua.sinoptik.ua/погода-луцьк')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_4(message):
    r = requests.get('https://ua.sinoptik.ua/погода-дніпро')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_5(message):
    r = requests.get('https://ua.sinoptik.ua/погода-донецьк')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_6(message):
    r = requests.get('https://ua.sinoptik.ua/погода-житомир')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_7(message):
    r = requests.get('https://ua.sinoptik.ua/погода-ужгород')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_8(message):
    r = requests.get('https://ua.sinoptik.ua/погода-запоріжжя')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_9(message):
    r = requests.get('https://ua.sinoptik.ua/погода-івано-франківськ')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_10(message):
    r = requests.get('https://ua.sinoptik.ua/погода-київ')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_11(message):
    r = requests.get('https://ua.sinoptik.ua/погода-кропивницький')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_12(message):
    r = requests.get('https://ua.sinoptik.ua/погода-луганск')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_13(message):
    r = requests.get('https://ua.sinoptik.ua/погода-львів')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_14(message):
    r = requests.get('https://ua.sinoptik.ua/погода-миколаїв')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_15(message):
    r = requests.get('https://ua.sinoptik.ua/погода-одеса')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_16(message):
    r = requests.get('https://ua.sinoptik.ua/погода-полтава')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_17(message):
    r = requests.get('https://ua.sinoptik.ua/погода-рівне')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_18(message):
    r = requests.get('https://ua.sinoptik.ua/погода-суми')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_19(message):
    r = requests.get('https://ua.sinoptik.ua/погода-тернопіль')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_20(message):
    r = requests.get('https://ua.sinoptik.ua/погода-харків')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_21(message):
    r = requests.get('https://ua.sinoptik.ua/погода-херсон')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_22(message):
    r = requests.get('https://ua.sinoptik.ua/погода-каменец-подольский')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_23(message):
    r = requests.get('https://ua.sinoptik.ua/погода-черкаси')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_24(message):
    r = requests.get('https://ua.sinoptik.ua/погода-чернівці')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)

def weather_25(message):
    r = requests.get('https://ua.sinoptik.ua/погода-чернігів')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    bot.send_message(message.chat.id, 'Погода на сьогодні:\n' +
                     t_min + ', ' + t_max + '\n' + text)
