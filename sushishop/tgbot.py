import telebot
from decouple import config

bot = telebot.TeleBot(config('BOT_TOKEN'))


def tg_send_order(message):
    bot.send_message(215750267, message)


def check_new_updates():
    updates = bot.get_updates()
    for update in updates:
        print(update)
