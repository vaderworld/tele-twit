import telebot

from telegram import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['/send'])
def send_to_twitter(message):
    pass


@bot.message_handler(commands=['/get'])
def get_from_twitter(amount):
    pass

if __name__ == '__main__':
    bot.polling(none_stop=True)
