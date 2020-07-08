import telebot

token = '1164004136:AAHQWSbIHwKlvcP1MeRyzZPyNXlEFJvVCuw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Бот запущен')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Доступные команды:')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, 'Не понимаю о чем вы')


bot.polling()
