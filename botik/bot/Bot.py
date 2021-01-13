
import imaplib
import email
from datetime import datetime
import html2text
from os import path
from email.header import decode_header, make_header


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('dasha@hicell.tel', 'DashaGerman19')
mail.list()
# Выводит список папок в почтовом ящике.
# result, data = mail.search(None, "ALL")
result, data = mail.select("inbox")
if result != 'OK':
    raise Exception("Error reading inbox: {}".format(data))
if data == ['0']:
    print(None)
latest = data[0].split()[-1]
result, data = mail.uid('fetch', latest, '(RFC822)')
if result != 'OK':
    raise Exception("Error reading email: {}".format(data))
# if delete ==True:
#     mail.store(latest, '+FLAGS', '\\Deleted')
message = email.message_from_bytes((data[0][1]))
print(data[0][1])
res = {
    'From': email.utils.parseaddr(message['From'])[1],
    'From name': email.utils.parseaddr(message['From'])[0],
    'Time': datetime.fromtimestamp(email.utils.mktime_tz(
        email.utils.parsedate_tz(message['Date']))),
    'To': message['To'],
    'Subject': str(make_header(decode_header(message["Subject"]))),
    'Text': '',
    'File': None
}
message_1 = email.message_from_bytes(data[0][1])
for part in message_1.walk():
    if part.get_content_maintype() == 'multipart':
        continue
    if part.get_content_maintype() == 'text':
        # reading as HTML (not plain text)
        _html = part.get_payload(decode=True)
        res['Text'] = html2text.html2text(_html.decode())
    # elif part.get_content_maintype() == 'application' and part.get_filename():
    #     fname = path.join("your/folder", part.get_filename())
    #     attachment = open(fname, 'wb')
    #     attachment.write(part.get_payload(decode = True))
    #     attachment.close()
    #     if res['File']:
    #         res['File'].append(fname)
    #     else:
    #         res['File'] = [fname]
res = f'{res["From name"]} \" {res["From"]} \" \n' \
      f'{res["Time"]} \n' \
      f'{res["Subject"]} \n' \
      # f'Text: {res["Text"]}'


# import telebot
# bot = telebot.TeleBot('1462574234:AAHBZLLLZ2V3BJKWroScV1vGOtmXs2dGg-A')
# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('Check', 'Пока')
#
#
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'check':
#         bot.send_message(message.chat.id, Readpost(), reply_markup=keyboard1)
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')
#
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
#
# bot.polling()

