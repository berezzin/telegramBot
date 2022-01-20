import telebot
from myParser import MyParser
import json

bot = telebot.TeleBot('5087141211:AAGOKkuVmk3bCOewKsNYjAnz3sf6FJiFT3g')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Какой товар ищете?")
        bot.register_next_step_handler(message, parsing)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


def parsing(item_to_found):
    n = 1
    MyParser.parse(item_to_found.text)
    bot.send_message(item_to_found.from_user.id, "Данные готовы в файле с форматом .json")
    with open(f'jsonFiles/{item_to_found.text}_21vek.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        for n, item in enumerate(data, start=n):
            bot.send_message(item_to_found.from_user.id,
                             f"№{str(n)}\n"
                             f"Название товара: {item['itemName']}\n"
                             f"Ссылка на товар: {item['itemLink']}\n"
                             f"Цена: {item['itemPrice']}")
            if n == 10:
                break


bot.polling(none_stop=True, interval=0)
