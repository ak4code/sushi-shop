import telebot
from pprint import pprint
from decouple import config

bot = telebot.TeleBot(config('BOT_TOKEN'))

