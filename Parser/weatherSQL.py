import tabulate
import requests
from bs4 import BeautifulSoup
import numpy as np

import sqlite3

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
q = 0
table1 = [['Месяц', 'День', 'Минимум', 'Максимум', 'Средняя', 'Дисперсия', 'Ночь', 'Минимум', 'Максимум', 'Средняя', 'Дисперсия']]
table2 = [['Месяц', 'День', 'Минимум', 'Максимум', 'Средняя', 'Ночь', 'Минимум', 'Максимум', 'Средняя']]

def parser(url, switch):
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
    if switch == 0:
        global q
        insert(year[q], monthDAY, monthNIGHT)
        q += 1
    return monthDAY, monthNIGHT

def info(monthDAY, monthNIGHT):
    return monthDAY.min(), monthDAY.max(), monthDAY.mean(), monthDAY.var(), monthNIGHT.min(), monthNIGHT.max(),\
           monthNIGHT.mean(), monthNIGHT.var()

def create():
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS weather (
                   month TEXT NOT NULL,
                   date INT NOT NULL,
                   day FLOAT NOT NULL,
                   night FLOAT NOT NULL
                );""")
    con.commit()
    print("Table was created")
create()

def insert(month, DAY, NIGHT):
    for i in range(len(DAY)):
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        cur.execute(f"INSERT INTO weather ("
                    f"month, date, day, night) VALUES (?, ?, ?, ?);", (month, i+1, int(DAY[i]), int(NIGHT[i])))
        con.commit()
    print(f"{len(DAY)} students were added")
# ---------------------------------------------------------------------------------------------------------------------
def select():
    mass = []
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    for i in year:
        mas = []
        for j in ['min(day)', 'max(day)', 'avg(day)', 'min(night)', 'max(night)', 'avg(night)']:
            cur.execute(f"select {j} as znachenie from weather where month = '{i}'")
            srDAYtemt = cur.fetchall()
            mas.append(round(srDAYtemt[0][0], 1))
        mass.append(mas)
    return mass

mode = input()
if mode == 'all': switch = 0
elif mode == 'baseinfo': switch = 1
elif mode == 'chek': switch = 2
elif mode == 'select': switch = 3
else: print("error")

if switch == 3:
    print('Вычисление с помощью SQL')
    data = select()
    co = 0
    for i in data:
        minnD, maxxD, avggD, minnN, maxxN, avggN = i
        if maxxD > 0: maxxD = '+' + str(maxxD)
        if minnD > 0: minnD = '+' + str(minnD)
        if avggD > 0:
            avggD = '+' + str("%.1f" % avggD)
        else:
            avggD = str("%.1f" % avggD)
        if maxxN > 0: maxxN = '+' + str(maxxN)
        if minnN > 0: minnN = '+' + str(minnN)
        if avggN > 0:
            avggN = '+' + str("%.1f" % avggN)
        else:
            avggN = str("%.1f" % avggN)
        table2.append([year[co], '☼', minnD, maxxD, avggD, '☾', minnN, maxxN, avggN])
        co += 1
    print(tabulate.tabulate(table2, tablefmt="grid", stralign='center'))

if switch != 3:
    for m in year:
        monthDAY, monthNIGHT = parser(spisokurl[n], switch)
        if switch == 0 or 2:
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
            table1.append([m, '☼', minnD, maxxD, avggD, str("%.2f" % varrD), '☾', minnN, maxxN, avggN, str("%.2f" % varrN)])

    if switch == 0 or 2:
        print('Вычисление с помощью Python + numpy')
        print(tabulate.tabulate(table1, tablefmt="grid", stralign='center'))