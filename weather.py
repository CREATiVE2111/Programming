import tabulate
import requests
from bs4 import BeautifulSoup
import numpy as np
np.set_printoptions(threshold=None)


spisokurl = ['https://pogoda.mail.ru/prognoz/brest_belarus/january-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/february-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/march-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/april-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/may-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/june-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/july-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/august-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/september-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/october-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/november-2022/',\
             'https://pogoda.mail.ru/prognoz/brest_belarus/december-2022/']

year = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
n = 0
data = [['Месяц', 'День', 'Минимум', 'Максимум', 'Средняя', 'Дисперсия', 'Ночь', 'Минимум', 'Максимум', 'Средняя', 'Дисперсия']]

def parser(url):
    rowdata = []; fp = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all(class_ = "day__temperature")
    for quote in quotes:
        rowdata.append(quote.text)
    for i in rowdata:
        fp.append(i.split())
    month = np.array(list(map(int, [word.rstrip("°") for word in sum(fp,[])])))
    monthDAY = month[0::2]
    monthNIGHT = month[1::2]
    return monthDAY, monthNIGHT

def info(monthDAY, monthNIGHT):
    return monthDAY.min(), monthDAY.max(), float(monthDAY.mean()), monthDAY.var(), monthNIGHT.min(), monthNIGHT.max(), float(monthNIGHT.mean()), monthNIGHT.var()

for m in year:
    monthDAY, monthNIGHT = parser(spisokurl[n])
    n += 1
    minnD, maxxD, avggD, varrD, minnN, maxxN, avggN, varrN = (info(monthDAY, monthNIGHT))
    if maxxD > 0: maxxD = '+' + str(maxxD)
    if minnD > 0: minnD = '+' + str(minnD)
    if avggD > 0: avggD = '+' + str("%.1f" % avggD)
    else: avggD = str("%.1f" % avggD)
    if maxxN > 0: maxxN = '+' + str(maxxN)
    if minnN > 0: minnN = '+' + str(minnN)
    if avggN > 0: avggN = '+' + str("%.1f" % avggN)
    else: avggN = str("%.1f" % avggN)
    data.append([m, '☼', minnD, maxxD, avggD, str("%.2f" % varrD), '☾', minnN, maxxN, avggN, str("%.2f" % varrN)])

print(tabulate.tabulate(data, tablefmt="grid", stralign='center'))
