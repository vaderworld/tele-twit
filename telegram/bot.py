import telebot

from twitter.bot import TwitterInteractor

from telegram import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['/send'])
def send_to_twitter(message):
    twitter.send_message(message)


@bot.message_handler(commands=['/get'])
def get_from_twitter(amount):
    print('received get request')
    tweets = twitter.get_messages(amount)
    bot.send_message(amount.chat.id, tweets)

if __name__ == '__main__':
    twitter = TwitterInteractor()
    bot.polling(none_stop=True)
