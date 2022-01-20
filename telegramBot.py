import telebot
from telebot import types
from myParser import MyParser

bot = telebot.TeleBot('5087141211:AAGOKkuVmk3bCOewKsNYjAnz3sf6FJiFT3g')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Какой товар ищете?")
        bot.register_next_step_handler(message, parsing)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


def parsing(item_to_found):
    MyParser.parse(item_to_found.text)
    bot.send_message(item_to_found.from_user.id, "Данные готовы в файле с форматом .json")


bot.polling(none_stop=True, interval=0)
