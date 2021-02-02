
import imaplib
import email
from datetime import datetime
import html2text
from os import path
from email.header import decode_header, make_header

def mail_post():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('dasha@hicell.tel', 'DashaGerman19')
    mail.select()
    return mail


mail_read_post = mail_post()
# mail = imaplib.IMAP4_SSL('imap.gmail.com')
# mail.login('support@hicell.tel', 'cldvuwspnpstodiw')
# mail.select()
# Выводит список папок в почтовом ящике.
result, data = mail_read_post.search(None, "ALL")
# result, data = mail.select("inbox")
# if result != 'OK':
#     raise Exception("Error reading inbox: {}".format(data))
# if data == ['0']:
#     print(None)
# latest = data[0].split()[-1]
# e_id = latest.decode('utf-8')
# result, data = mail.uid('fetch', e_id, '(RFC822)')
# uid = str(data[0][0]).split(' ')
# print(uid)

typ, msg_data = mail_read_post.fetch(
    (data[0].split())[-1].decode('utf-8'), '(RFC822)')
uid = (str(msg_data[0]).split('\'')[1].split(' '))[0]
message = email.message_from_bytes((msg_data[0][1]))
print(message)

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
        elif part.get_content_maintype() == 'application' and part.get_filename():
            # fname = path.join("/bot_image", part.get_filename())
            # attachment = open(fname, 'wb')
            # attachment.write(part.get_payload(decode = True))
            # attachment.close()
            filename = part.get_filename()
            if filename:
                # Нам плохого не надо, в письме может быть всякое барахло
                with open(part.get_filename(), 'w') as new_file:
                    new_file.write(
                        str(part.get_payload(decode=True), encoding='utf-8'))
                    new_file.close()
            text1.append(filename)
            # if res['File']:
            #     res['File'].append(fname)
            # else:
            #     res['File'] = [fname]
        return text1

print(get_text(uid))
# result, data = mail.search(None, 'All')
# # labels = ['bot']
# # types, response = mail.store(data[0].split()[900],
# #                                        '+FLAGS',
# #                                        r'(%s)' % (labels[0]))
# type, ready = mail.fetch(data[0].split()[900], '(FLAGS)')
#
# print(ready[0])
# uid = (str(data[0]).split('\''))[1].split(' ')
# print(len(uid))
# i=0
# while i<len(uid)-2313:
#     typ, msg_data = mail.fetch(data[0].split()[i], '(RFC822)')
#     uid1 = (str(msg_data[0]).split('\'')[1].split(' '))[0]
#     print(uid1)
#     i+=1
# uid = (str(data[0]).split('\''))[1].split(' ')
# print(len(uid))
# type, ready = mail.fetch(latest, '(RFC822)')
# print((str(ready[0]).split('\'')[1].split(' '))[0])
# result, data = mail.fetch(uid[2], "(RFC822)")  # Получаем тело письма (RFC822) для данного ID
# raw_email = data[0][1]
# print(raw_email)
# if result != 'OK':
#     raise Exception("Error reading email: {}".format(data))
# # if delete ==True:
# #     mail.store(latest, '+FLAGS', '\\Deleted')
# message = email.message_from_bytes((data[0][1]))
# # print(data[0][1])
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
#     # elif part.get_content_maintype() == 'application' and part.get_filename():
#     #     fname = path.join("your/folder", part.get_filename())
#     #     attachment = open(fname, 'wb')
#     #     attachment.write(part.get_payload(decode = True))
#     #     attachment.close()
#     #     if res['File']:
#     #         res['File'].append(fname)
#     #     else:
#     #         res['File'] = [fname]
# res = f'{res["From name"]} \" {res["From"]} \" \n' \
#       f'{res["Time"]} \n' \
#       f'{res["Subject"]} \n' \
#       # f'Text: {res["Text"]}'
#
#
# # import telebot
# # bot = telebot.TeleBot('1462574234:AAHBZLLLZ2V3BJKWroScV1vGOtmXs2dGg-A')
# # keyboard1 = telebot.types.ReplyKeyboardMarkup()
# # keyboard1.row('Check', 'Пока')
# #
# #
# # @bot.message_handler(content_types=['text'])
# # def send_text(message):
# #     if message.text.lower() == 'check':
# #         bot.send_message(message.chat.id, Readpost(), reply_markup=keyboard1)
# #     elif message.text.lower() == 'пока':
# #         bot.send_message(message.chat.id, 'Прощай, создатель')
# #
# #
# #
# # @bot.message_handler(commands=['start'])
# # def start_message(message):
# #     bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
# #
# # bot.polling()
#
