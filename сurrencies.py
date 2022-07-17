import telebot
import requests
from bs4 import BeautifulSoup as BS

TOREN = "5486552502:AAFLX5MbQ6jpA75sD0lEjHdsUeLtIPE5-UY"

bot = telebot.TeleBot(TOREN)

def course_USD(message):
    url = 'https://minfin.com.ua/currency/usd/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('table', {'class': 'table-response'})
    tr = table.find('td', {'class': 'mfm-text-nowrap'})
    tr =tr.text
    tr = tr[:7]

    bot.send_message(message.chat.id, 'Курс USD: ' + str(tr))

def course_EUR(message):
    url = 'https://minfin.com.ua/currency/eur/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('table', {'class': 'table-response'})
    tr = table.find('td', {'class': 'mfm-text-nowrap'})
    tr =tr.text
    tr = tr[:7]

    bot.send_message(message.chat.id, 'Курс EUR: '  + str(tr))

def course_RUB(message):
    url = 'https://minfin.com.ua/currency/rub/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('table', {'class': 'table-response'})
    tr = table.find('td', {'class': 'mfm-text-nowrap'})
    tr =tr.text
    tr = tr[:7]

    bot.send_message(message.chat.id, 'Курс RUB: '  + str(tr))

def course_PLN(message):
    url = 'https://minfin.com.ua/ua/currency/banks/pln/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('table', {'class': 'table-response'})
    tr = table.find('td', {'class': 'mfm-text-nowrap'})
    tr =tr.text
    tr = tr[:7]

    bot.send_message(message.chat.id, 'Курс PLN: '  + str(tr))

def course_GBP(message):
    url = 'https://minfin.com.ua/ua/currency/gbp/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('table', {'class': 'table-response'})
    tr = table.find('td', {'class': 'mfm-text-nowrap'})
    tr =tr.text
    tr = tr[:7]

    bot.send_message(message.chat.id, 'Курс GBP: '  + str(tr))

def course_CHF(message):
    url = 'https://minfin.com.ua/ua/currency/chf/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('table', {'class': 'table-response'})
    tr = table.find('span', {'class': 'mfm-posr'})
    tr =tr.text
    tr = tr[:6]

    bot.send_message(message.chat.id, 'Курс CHF: '  + str(tr))

def course_BTC(message):
    url = 'https://minfin.com.ua/ua/currency/crypto/bitcoin/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('div', {'class': 'sc-18a2k5w-7 jLhBcj'})
    tr = table.find('div', {'class': 'sc-18a2k5w-1 hpFLcm'})
    tr =tr.text
    tr = tr[:7]

    bot.send_message(message.chat.id, 'Курс Bitcoin: '  + str(tr))

def course_ETH(message):
    url = 'https://minfin.com.ua/ua/currency/crypto/ethereum/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('div', {'class': 'sc-18a2k5w-7 jLhBcj'})
    tr = table.find('div', {'class': 'sc-18a2k5w-1 hpFLcm'})
    tr =tr.text
    tr = tr[:6]

    bot.send_message(message.chat.id, 'Курс Ethereum: '  + str(tr))

def course_BNB(message):
    url = 'https://minfin.com.ua/ua/currency/crypto/binancecoin/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('div', {'class': 'sc-18a2k5w-7 jLhBcj'})
    tr = table.find('div', {'class': 'sc-18a2k5w-1 hpFLcm'})
    tr =tr.text
    tr = tr[:6]

    bot.send_message(message.chat.id, 'Курс BNB: '  + str(tr))

def course_DOGE(message):
    url = 'https://minfin.com.ua/ua/currency/crypto/dogecoin/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('div', {'class': 'sc-18a2k5w-7 jLhBcj'})
    tr = table.find('div', {'class': 'sc-18a2k5w-1 hpFLcm'})
    tr =tr.text
    tr = tr[:7]

    bot.send_message(message.chat.id, 'Курс Dogecoin: '  + str(tr))

def course_SHIB(message):
    url = 'https://minfin.com.ua/ua/currency/crypto/shiba-inu/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('div', {'class': 'sc-18a2k5w-7 jLhBcj'})
    tr = table.find('div', {'class': 'sc-18a2k5w-1 hpFLcm'})
    tr =tr.text
    tr = tr[:11]

    bot.send_message(message.chat.id, 'Курс Shiba Inu: '  + str(tr))

def course_LTC(message):
    url = 'https://minfin.com.ua/ua/currency/crypto/litecoin/'

    source = requests.get(url)
    main_text = source.text
    soup = BS(main_text)

    table = soup.find('div', {'class': 'sc-18a2k5w-7 jLhBcj'})
    tr = table.find('div', {'class': 'sc-18a2k5w-1 hpFLcm'})
    tr =tr.text
    tr = tr[:6]

    bot.send_message(message.chat.id, 'Курс Litecoin: '  + str(tr))