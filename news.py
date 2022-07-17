import telebot
import requests
from bs4 import BeautifulSoup as BS

TOREN = "5486552502:AAFLX5MbQ6jpA75sD0lEjHdsUeLtIPE5-UY"

bot = telebot.TeleBot(TOREN)

def science_and_technology(message):
    response = requests.get("https://focus.ua/technologies")

    soup = BS(response.content, "html.parser")
    a_title = soup.find_all("a", class_="c-card__link")
    a_titles = a_title[:4]

    for element in a_titles:
        bot.send_message(message.chat.id, element['href'])

def digital(message):
    response = requests.get("https://focus.ua/digital")

    soup = BS(response.content, "html.parser")
    a_title = soup.find_all("a", class_="c-card__link")
    a_titles = a_title[:4]

    for element in a_titles:
        bot.send_message(message.chat.id, element['href'])

def ukraine(message):
    response = requests.get("https://focus.ua/ukraine")

    soup = BS(response.content, "html.parser")
    a_title = soup.find_all("a", class_="c-card__link")
    a_titles = a_title[:4]

    for element in a_titles:
        bot.send_message(message.chat.id, element['href'])

