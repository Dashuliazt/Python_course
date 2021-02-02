from multiprocessing import Pool
#подключения библиотек
import http.client
import requests
import mysql.connector
import ssl
import datetime



def f(con_cod):
    now = datetime.datetime.now()
    # цикл перебиарет номера
    i = 0
    r = requests.get(
        'https://hidemy.name/api/proxylist.txt?out=plain&country=ALARAMATBDBYBOBABRBGBIKHCACLCOCDCZECFIFRGEDEHNHKHUINIDIRIQITJPKEKRLVMKMWMYMXMDMZNPNLNINENGPKPSPYPEPLRORSSGSKZAESSECHTWTHTRUAAEGBVEVN&maxtime=1000&type=hs&'
        'maxtime=1000&code=662967421859502')
    # r = requests.get('https://hidemy.name/api/proxylist.txt?out=plain&country=UAGEFR&type=hs&maxtime=2000&'
    #                  'code=662967421859502')
    spisok = r.text.split('\r\n')[i]
    k = len(r.text.split('\r\n'))
    print('Start' + spisok)
    host = spisok.split(':', )[:1]
    host = host[0]
    port = spisok.split(':', )[1:]
    port = port[0]
    # подключение к базе 1026065
    cnx = mysql.connector.connect(user='pma', password='pma', host='127.0.0.1',
                                  database='python_test1',
                                  connection_timeout=7200)
    result = []
    num = 5604675
    num_max = num + 5
    while num != num_max:
        # формирования номера в виде строки для запроса
        phone = '0' + str(con_cod) + str(num)
        print(phone)
        # запрос на список прокси по странам Германия, Россия Украина
        try:
            # формирования запроса
            payload = 'number=' + phone
            headers = {
                'X-OCTOBER-REQUEST-HANDLER': 'onMobileTransferSearch',
                'X-Requested-With': 'XMLHttpRequest',
                'Host': 'www.ucrf.gov.ua',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'cookiesession1=2AE42CE6IETPSROE2OBUG19KIOIC9DC5'
            }
            conn = http.client.HTTPSConnection(host, port, timeout=5,
                                               context=ssl._create_unverified_context())
            conn.set_tunnel("www.ucrf.gov.ua")
            conn.request("POST", "/ua/services/transfer-mobile-search",
                         payload, headers)
            res = conn.getresponse()
            data = res.read()
            # print(data)

        except OSError:
            if i < k - 2:
                i = i + 1
                spisok = r.text.split('\r\n')[i]
                print('Error OS' + spisok)
                host = spisok.split(':', )[:1]
                host = host[0]
                port = spisok.split(':', )[1:]
                port = port[0]
                continue
            else:
                i = 0
                spisok = r.text.split('\r\n')[i]
                print('начали сначала' + spisok)
                host = spisok.split(':', )[:1]
                host = host[0]
                port = spisok.split(':', )[1:]
                port = port[0]
                continue

        except:
            if i < k - 2:
                i = i + 1
                spisok = r.text.split('\r\n')[i]
                print('общай ошибка' + spisok)
                host = spisok.split(':', )[:1]
                host = host[0]
                port = spisok.split(':', )[1:]
                port = port[0]
                continue
            else:
                i = 0
                spisok = r.text.split('\r\n')[i]
                print('начали сначала общая ошибка' + spisok)
                host = spisok.split(':', )[:1]
                host = host[0]
                port = spisok.split(':', )[1:]
                port = port[0]
                continue

                # проверка по классу ответа

        if 'alert-success' in data.decode('UTF-8'):
            # номер найден
            answer = data.decode('UTF-8').replace('<\\', '<').encode().decode(
                'unicode-escape')
            answer = answer.split('<span>')
            answer = answer[1]
            answer = answer.split('</span>')
            # answer - полный ответ (description)
            answer = answer[0]
            phone = answer.split(' ')
            # - только
            answer = answer[61:-1]
            print(answer)
            print(type(answer))
            my_dict = {'КИЇВСТАР': '25503', 'Lifecell': '25506',
                       'Vodafone Україна': '25501'}
            if answer in my_dict:
                answer = my_dict[answer]
            # - только номер телефона
            phone = phone[2]
            status = 'present'
            result.append(answer)
            print('перенесённый' + phone)

        else:
            # номер отсутствует
            answer = data.decode('UTF-8').replace('<\\', '<').encode().decode(
                'unicode-escape')
            answer = answer.split('<span>')
            answer = answer[1]
            answer = answer.split('</span>')
            # answer - полный ответ (description)
            answer = answer[0]
            phone = answer.split(' ')
            # - только номер телефона
            phone = phone[2]
            status = 'absent'
            result.append(answer)
            print('не перенесённый ' + phone)
        if status == 'present':
            # формирования запроса в базу данных (вставка данных)
            sql = """INSERT INTO numbers (number, mccmnc, date) VALUES (%s,%s,%s)"""
            val = [phone, answer, now]
            cursor = cnx.cursor()
            cursor.execute(sql, val)
            cnx.commit()
            num = num + 1
            cursor.close()
            cnx.close()
        else:
            num = num + 1
            print('_________________')

if __name__ == '__main__':
    p = Pool(15)
    print(p.map(f, [66, 99, 95, 50, 68, 67, 96, 97, 98, 39, 94, 63, 73, 93, 91]))




#     # подключения библиотек
# import http.client
# import requests
# import mysql.connector
# import ssl
# import datetime
#
# now = datetime.datetime.now()
# # цикл перебиарет номера
# i = 0
# r = requests.get(
#     'https://hidemy.name/api/proxylist.txt?out=plain&country=ALARAMATBDBYBOBABRBGBIKHCACLCOCDCZECFIFRGEDEHNHKHUINIDIRIQITJPKEKRLVMKMWMYMXMDMZNPNLNINENGPKPSPYPEPLRORSSGSKZAESSECHTWTHTRUAAEGBVEVN&maxtime=1000&type=hs&'
#     'maxtime=1000&code=662967421859502')
# # r = requests.get('https://hidemy.name/api/proxylist.txt?out=plain&country=UAGEFR&type=hs&maxtime=2000&'
# #                  'code=662967421859502')
# spisok = r.text.split('\r\n')[i]
# k = len(r.text.split('\r\n'))
# print('Start' + spisok)
# host = spisok.split(':', )[:1]
# host = host[0]
# port = spisok.split(':', )[1:]
# port = port[0]
# # подключение к базе 1026065
# cnx = mysql.connector.connect(user='pma', password='pma', host='127.0.0.1',
#                               database='python_test1', connection_timeout=7200)
# result = []
# country_code = '0'
# num = int(input(
#     'Введите код оператора без 0 и начало диапазона, пример: 660000066 : '))
# num_max = num + 1000
# while num != num_max:
#     # формирования номера в виде строки для запроса
#     phone = country_code + str(num)
#     print(phone)
#     # запрос на список прокси по странам Германия, Россия Украина
#     try:
#         # формирования запроса
#         payload = 'number=' + phone
#         headers = {
#             'X-OCTOBER-REQUEST-HANDLER': 'onMobileTransferSearch',
#             'X-Requested-With': 'XMLHttpRequest',
#             'Host': 'www.ucrf.gov.ua',
#             'Content-Length': '17',
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Cookie': 'cookiesession1=2AE42CE6IETPSROE2OBUG19KIOIC9DC5'
#         }
#         conn = http.client.HTTPSConnection(host, port, timeout=5,
#                                            context=ssl._create_unverified_context())
#         conn.set_tunnel("www.ucrf.gov.ua")
#         conn.request("POST", "/ua/services/transfer-mobile-search", payload,
#                      headers)
#         res = conn.getresponse()
#         data = res.read()
#         print(data)
#
#     except OSError:
#         if i < k - 2:
#             i = i + 1
#             spisok = r.text.split('\r\n')[i]
#             print('Error OS' + spisok)
#             host = spisok.split(':', )[:1]
#             host = host[0]
#             port = spisok.split(':', )[1:]
#             port = port[0]
#             continue
#         else:
#             i = 0
#             spisok = r.text.split('\r\n')[i]
#             print('начали сначала' + spisok)
#             host = spisok.split(':', )[:1]
#             host = host[0]
#             port = spisok.split(':', )[1:]
#             port = port[0]
#             continue
#
#     except:
#         if i < k - 2:
#             i = i + 1
#             spisok = r.text.split('\r\n')[i]
#             print('общай ошибка' + spisok)
#             host = spisok.split(':', )[:1]
#             host = host[0]
#             port = spisok.split(':', )[1:]
#             port = port[0]
#             continue
#         else:
#             i = 0
#             spisok = r.text.split('\r\n')[i]
#             print('начали сначала общая ошибка' + spisok)
#             host = spisok.split(':', )[:1]
#             host = host[0]
#             port = spisok.split(':', )[1:]
#             port = port[0]
#             continue
#
#             # проверка по классу ответа
#
#     if 'alert-success' in data.decode('UTF-8'):
#         # номер найден
#         answer = data.decode('UTF-8').replace('<\\', '<').encode().decode(
#             'unicode-escape')
#         answer = answer.split('<span>')
#         answer = answer[1]
#         answer = answer.split('</span>')
#         # answer - полный ответ (description)
#         answer = answer[0]
#         phone = answer.split(' ')
#         # - только
#         answer = answer[61:-1]
#         print(answer)
#         print(type(answer))
#         my_dict = {'КИЇВСТАР': '25503', 'Lifecell': '25506',
#                    'Vodafone Україна': '25501'}
#         if answer in my_dict:
#             answer = my_dict[answer]
#         # - только номер телефона
#         phone = phone[2]
#         status = 'present'
#         result.append(answer)
#         print('перенесённый' + phone)
#
#     else:
#         # номер отсутствует
#         answer = data.decode('UTF-8').replace('<\\', '<').encode().decode(
#             'unicode-escape')
#         answer = answer.split('<span>')
#         answer = answer[1]
#         answer = answer.split('</span>')
#         # answer - полный ответ (description)
#         answer = answer[0]
#         phone = answer.split(' ')
#         # - только номер телефона
#         phone = phone[2]
#         status = 'absent'
#         result.append(answer)
#         print('не перенесённый ' + phone)
#     if status == 'present':
#         # формирования запроса в базу данных (вставка данных)
#         sql = """INSERT INTO numbers (number, mccmnc, date) VALUES (%s,%s,%s)"""
#         val = [phone, answer, now]
#         cursor = cnx.cursor()
#         cursor.execute(sql, val)
#         cnx.commit()
#         num = num + 1
#         cursor.close()
#         cnx.close()
#     else:
#         num = num + 1
#
# print(num)
# # cursor.close()
# # cnx.close()
#


