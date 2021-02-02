import telebot

bot = telebot.TeleBot('1462574234:AAHBZLLLZ2V3BJKWroScV1vGOtmXs2dGg-A')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()