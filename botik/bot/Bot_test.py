import imaplib
import email
from datetime import datetime
import html2text
from os import path
from email.header import decode_header, make_header
import telebot
from telebot import types






def mail_post():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('support@hicell.tel', 'cldvuwspnpstodiw')
    mail.select()
    return mail


def Readpost():
    mail_read_post = mail_post()
    try:
        # Выполняет поиск и возвращает UID писем.
        result, data = mail_read_post.search(None, 'ALL')
        if result != 'OK':
            raise Exception("Error reading inbox: {}".format(data))
        if data == ['0']:
            return 'None'
        uid_total = (str(data[0]).split('\''))[1].split(' ')
        labels = ['bot']
        i = -1
        res1 = []
        uid1 = []
        while i > -len(uid_total):
            type, ready = mail_read_post.fetch(data[0].split()[i], '(FLAGS)')
            print(ready[0])
            if str(ready[0]).find(labels[0])>0:
                break
            else:
                typ, msg_data = mail_read_post.fetch(
                    (data[0].split()[i]).decode('utf-8'), '(RFC822)')
                uid = (str(msg_data[0]).split('\'')[1].split(' '))[0]
                message = email.message_from_bytes((msg_data[0][1]))
                res = {
                    'From': email.utils.parseaddr(message['From'])[1],
                    'From name': email.utils.parseaddr(message['From'])[0],
                    'Time': datetime.fromtimestamp(email.utils.mktime_tz(
                        email.utils.parsedate_tz(message['Date']))),
                    'To': message['To'],
                    'Subject': str(
                        make_header(decode_header(message["Subject"]))),
                    'Text': '',
                    'File': None
                }
                types, response = mail_read_post.store(data[0].split()[i],
                                             '+FLAGS',
                                             r'(%s)' % (labels[0]))
                res = f'{res["From name"]} \" {res["From"]} \" \n' \
                  f'{res["Time"]} \n' \
                  f'{res["Subject"]}'
                res1.append(res)
                uid1.append(uid)
                i -= 1

        if len(res1) == 0:
            return 'New messages is not found'
        else:
            return res1, uid1
    except ValueError:
        return 'error'


def get_text(uid):
    mail_read_post = mail_post()
    typ, msg_data = mail_read_post.fetch(uid, '(RFC822)')
    message = email.message_from_bytes((msg_data[0][1]))
    text1=[]
    for part in message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get_content_maintype() == 'text':
            # reading as HTML (not plain text)
            _html = part.get_payload(decode=True)
            text = html2text.html2text(_html.decode())
            text1.append(text)
        # if part.get_content_maintype() == 'image':
        #     _image=part.get_filename()
        #     text1.append(_image)
        return text1


# Подключение бота
# bot = telebot.TeleBot('1462574234:AAHBZLLLZ2V3BJKWroScV1vGOtmXs2dGg-A')
bot = telebot.TeleBot('1611646416:AAGSw1S9Catrw7zZsVOyEPsyyBOJjn3OtPA')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Check', 'Help')
user_id = [391182955, 469481549, 249093185]



@bot.message_handler(commands=['start'])
def start_message(message):

    user = message.from_user
    if user.id in user_id:
        bot.send_message(message.chat.id,
                         f'Welcome, {user.first_name} to Support Bot!',
                         reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id,
                         f'You {user.username} do not have access to the bot, '
                         f'contact the creator  !')


@bot.message_handler(func=lambda message: message.from_user.id not in user_id)
def auth(message):
    bot.send_message(message.chat.id, 'You do not have access to the bot, '
                                      'contact the creator !')

# def send_cron_text():
#     mess_data = Readpost()
#     if len(mess_data) == 2:
#         for j in range(len(mess_data[0])):
#             # bot.send_message(message.chat.id, Readpost()[j], reply_markup=keyboard1)
#             keyboard = types.InlineKeyboardMarkup()
#             # По очереди готовим текст и обработчик для каждого сообщения
#             key_j = types.InlineKeyboardButton(text='Text message', callback_data=f'{mess_data[1][j]}')
#             keyboard.add(key_j)
#             bot.send_message('391182955',
#                              f'{mess_data[0][j]}')
#     else:
#         bot.send_message('391182955', mess_data)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'check':
        mess_data = Readpost()
        if len(mess_data) == 2:
            for j in range(len(mess_data[0])):
                # bot.send_message(message.chat.id, Readpost()[j], reply_markup=keyboard1)
                keyboard = types.InlineKeyboardMarkup()
                # По очереди готовим текст и обработчик для каждого сообщения
                key_j = types.InlineKeyboardButton(text='Text message', callback_data=f'{mess_data[1][j]}')
                keyboard.add(key_j)
                bot.send_message(message.chat.id,
                                 f'{mess_data[0][j]}', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, mess_data)

    elif message.text.lower() == 'help':
        bot.send_message(message.chat.id,
                    'Bot create for checking support email. '
                    'If you want to connect with developer - dasha@hicell.net')


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    textik = get_text(call.data)
    # Отправляем текст в Телеграм
    if len(textik) > 4096:
        for x in range(0, len(textik), 4096):
            bot.send_message(call.message.chat.id, textik[x:x + 4096])
    else:
        bot.send_message(call.message.chat.id, textik)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)


# функция для проставления флага для всей почты
# def set_flags():
#     mail_read_post = mail_post()
#     result, data = mail_read_post.search(None, 'ALL')
#     uid_total = (str(data[0]).split('\''))[1].split(' ')
#     labels = ['bot']
#     ready1 = []
#     i = -1
#     while i > -1000:
#     # for i in range(7200,(len(uid_total)-1)):
#         type, ready = mail_read_post.fetch(data[0].split()[i], '(FLAGS)')
#         print(ready[0])
#         if str(ready[0]).find(labels[0]) > 0:
#             i -= 1
#         else:
#             types, response = mail_read_post.store(data[0].split()[i],
#                                            '+FLAGS',
#                                            r'(%s)' % (labels[0]))
#
#             i -= 1
#             ready1.append(ready)
#     return ready1
# mail_post().logout()
#
#
# print(set_flags())

