import imaplib
import email
from datetime import datetime
import html2text
from os import path
from email.header import decode_header, make_header
import telebot
from telebot import types

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])
def Readpost():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('dasha@hicell.tel', 'DashaGerman19')
    mail.select()
    # Выводит список папок в почтовом ящике.
    # result, data = mail.search(None, "ALL")
    try:
        result, data = mail.search(None, 'ALL') # Выполняет поиск и возвращает UID писем.
        if result != 'OK':
            raise Exception("Error reading inbox: {}".format(data))
        if data == ['0']:
            return 'None'
        labels = ['test23']
        i=-5
        res1 = []
        text1 = []
        while i < 0:
            type, ready = mail.fetch(data[0].split()[i], '(FLAGS)')
            if str(ready[0]).find(labels[0])>0:

                i +=1
            else:
                typ, msg_data = mail.fetch(data[0].split()[i], '(RFC822)')
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
                for part in message.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get_content_maintype() == 'text':
                        # reading as HTML (not plain text)
                        _html = part.get_payload(decode=True)
                        res['Text'] = html2text.html2text(_html.decode())
                types, response = mail.store(data[0].split()[i],
                                             '+FLAGS',
                                             r'(%s)' % (labels[0]))
                text = f'{res["Text"]}'
                text1.append(text)
                res = f'{res["From name"]} \" {res["From"]} \" \n' \
                  f'{res["Time"]} \n' \
                  f'{res["Subject"]}'
                res1.append(res)
                i += 1

        if len(res1) == 0:
            return 'New messages is not found'
        else:
            return res1, text1
    except ValueError:
        return 'error'



#print(len(Readpost()))
# print(len(Readpost()))
# print(Readpost())
#
#



bot = telebot.TeleBot('1462574234:AAHBZLLLZ2V3BJKWroScV1vGOtmXs2dGg-A')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Check', 'Пока')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'check':
        mess_data = Readpost()
        if len(mess_data) == 2:
            for j in range(len(mess_data[0])):
                # bot.send_message(message.chat.id, Readpost()[j], reply_markup=keyboard1)
                keyboard = types.InlineKeyboardMarkup()
                # По очереди готовим текст и обработчик для каждого сообщения
                key_j = types.InlineKeyboardButton(text='Text message', callback_data=f'textmess{j}')
                keyboard.add(key_j)
                bot.send_message(message.chat.id,
                                 f'{mess_data[0][j]}', reply_markup=keyboard)
                # bot.send_message(message.from_user.id, text='',
                #                  reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, mess_data)

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    j = int(str(call.data)[-1])
    if call.data == f"textmess{j}":
        #Формируем гороскоп
        msg = Readpost()[1][j]
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)


# latest_email_uid = data[0].split()[-1]
# for num in data[0].split():
#     # result, data = mail.fetch(num, '(RFC822)')
#     result, data = mail.uid('fetch', num, '(RFC822)')
# if result != 'OK':
#     raise Exception("Error reading email: {}".format(data))
# if data == ['0']:
#     print('None')
# if delete ==True:
#     mail.store(latest, '+FLAGS', '\\Deleted')
# message = email.message_from_bytes((data[0][1]))
# res = {
#     'From': email.utils.parseaddr(message['From'])[1],
#     'From name': email.utils.parseaddr(message['From'])[0],
#     'Time': datetime.fromtimestamp(email.utils.mktime_tz(
#         email.utils.parsedate_tz(message['Date']))),
#     'To': message['To'],
#     'Subject': str(make_header(decode_header(message["Subject"]))),
#     'Text': '',
#     'File': None
# }
# message_1 = email.message_from_bytes(data[0][1])
# for part in message_1.walk():
#     if part.get_content_maintype() == 'multipart':
#         continue
#     if part.get_content_maintype() == 'text':
#         # reading as HTML (not plain text)
#         _html = part.get_payload(decode=True)
#         res['Text'] = html2text.html2text(_html.decode())
# #     # elif part.get_content_maintype() == 'application' and part.get_filename():
# #     #     fname = path.join("your/folder", part.get_filename())
# #     #     attachment = open(fname, 'wb')
# #     #     attachment.write(part.get_payload(decode = True))
# #     #     attachment.close()
# #     #     if res['File']:
# #     #         res['File'].append(fname)
# #     #     else:
# #     #         res['File'] = [fname]
# #


# for response_part in msg_data:
#     if isinstance(response_part, tuple):
#         msg = email.message_from_bytes(response_part[1])
#         payload=msg.get_payload()
#         body=extract_body(payload)
#         res['Text'] = html2text.html2text(body)