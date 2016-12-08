import telebot
import config
from twitter.TwitterInteractor import TwitterInteractor

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def show_help(message):
    bot.send_message(message.chat.id, 'Commands:\n/send <msg> - send <msg> to twitter\n/get <n> - get <n> last tweets from timeline')

@bot.message_handler(commands=['send'])
def send_to_twitter(message):
    tweet_msg = message.text[len('/send '):]
    if len(tweet_msg) > 140:
        bot.send_message(message.chat.id, 'Your message has more than 140 symbols!')
    twitter.send_message(tweet_msg)


@bot.message_handler(commands=['get'])
def get_from_twitter(message):
    try:
        amount = int(message.text[len('/get '):])
    except ValueError:
        bot.send_message(message.chat.id, 'Please type proper amount')
        return
    tweets = twitter.get_messages(amount)
    for tweet in tweets:
        bot.send_message(message.chat.id, tweet)

if __name__ == '__main__':
    twitter = TwitterInteractor()
    bot.polling(none_stop=True)