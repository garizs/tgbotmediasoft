import telebot

token = '1164004136:AAHQWSbIHwKlvcP1MeRyzZPyNXlEFJvVCuw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Бот запущен')

bot.polling()