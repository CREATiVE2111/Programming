# распределить покупка продажа
import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
import sqlite3

def format(n):
    s = str(n)
    return s[2:-1]

def connect():
    username = "v.alesha_2004@mail.ru"
    mail_pass = "UMgjim2cwCR0MxQm96q0"
    mail = imaplib.IMAP4_SSL('imap.mail.ru')

    mail.login(username, mail_pass)
    mail.list()
    mail.select('inbox', readonly=False)
    result, data = mail.uid('search', None, "ALL"); result2, data2 = mail.search(None, "ALL")

    id_list = data[0].split(); id_list2 = data2[0].split()

    mail.select('Buy', readonly=False)
    resultB, dataB = mail.uid('search', None, "ALL")
    mail.select('Sell', readonly=False)
    resultS, dataS = mail.uid('search', None, "ALL")

    try:
        dataB = dataB[0].split()
        dataB = str(dataB[-1])[2:-1]
    except: pass
    try:
        dataS = dataS[0].split()
        dataS = str(dataS[-1])[2:-1]
    except: pass

    mail.select('inbox', readonly=False)

    for i in range(len(id_list)):
        id_list[i] = format(id_list[i])
    return mail, id_list, id_list2, dataB, dataS

def get_need_msg(mail_id, mail):
    result, data = mail.uid('fetch', mail_id, "(RFC822)")
    raw_mail = data[0][1]
    raw_mail_string = raw_mail.decode('utf-8', errors='ignore')

    mail_message = email.message_from_string(raw_mail_string)

    msg_header = email.utils.parseaddr(mail_message['From'])[1]
    if msg_header == 'udachainyou@mail.ru':
        get_inf_msg(raw_mail_string, mail_id)

def get_inf_msg(raw_mail_string, mail_id):
    mail_message = email.message_from_string(raw_mail_string)
    head_msg = decode_header(mail_message["Subject"])[0][0].decode()
    if head_msg == 'Магазинчик Электроники':
        if mail_message.is_multipart():
            for payload in mail_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8', errors='ignore')
            parser(body, mail_id)

def parser(body, mail_id):
    soup = BeautifulSoup(body, 'html.parser')
    try: price = soup.find_all('span', class_='price'); price = price[0].get_text(':')
    except: pass
    try: status = soup.find_all('span', class_='status'); status = status[0].get_text()
    except: pass
    else:
        if status == 'приобрели':
            sep(mail_id, id_list2, 'Buy')
        elif status == 'продали':
            sep(mail_id, id_list2, 'Sell')
    try: product = soup.find_all('span', class_='product'); product = product[0].get_text(':')
    except: pass
    try: add2table(product, price, status)
    except: print('error')

def create():
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute("SELECT tbl_name FROM sqlite_master where type='table'")
    tables = cur.fetchall()
    if tables == []:
        cur.execute("""CREATE TABLE IF NOT EXISTS storage (
                       product TEXT NOT NULL,
                       price INT NOT NULL,
                       status TEXT NOT NULL);""")
        con.commit()
        cur.execute(f"INSERT INTO storage (product, price, status) VALUES (?, ?, ?);", (' ', 0, '0'))
        con.commit()
        con.close()

def updcount(count, id):
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute(f"Update storage set price = {count} where product = ' '")
    cur.execute(f"Update storage set status = '{id}' where product = ' '")
    con.commit()
    con.close()

def add2table(product, price, status):
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO storage (product, price, status) VALUES (?, ?, ?);", (product, price, status[:-1]))
    con.commit()
    con.close()

def get_count():
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute("SELECT status FROM storage limit 1")
    count = cur.fetchall()
    con.commit()
    con.close()
    return count[0][0]

def analytics():
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute("SELECT sum(price) FROM storage where status = 'приобрел'")
    buy = cur.fetchall()
    cur.execute("SELECT sum(price) FROM storage where status = 'продал'")
    sell = cur.fetchall()
    try: summ = sell[0][0] - buy[0][0]; return(summ)
    except: pass

def sep(mail_id, id_list2, ch):
    mail_id = id_list2[id_list.index(mail_id)-1]
    copy_res = mail.copy(mail_id, ch)
    print(copy_res)
    if copy_res[0] == 'OK':
        delete_res = mail.store(mail_id, '+FLAGS', '\\Deleted')
    mail.expunge()

create()
mail, id_list, id_list2, dataB, dataS = connect()
count = int(get_count())
count = max(int(dataB), int(dataS), int(count))
for i in id_list:
    n = int(i)
    if n > count:
        count = int(id_list[id_list.index(i)-1])
        break
if count == 0:
    id_list.insert(0, '0')
print(count, int(id_list[-1]))
if count <= int(id_list[-1]):
    q = 0
    for i in range((len(id_list)-1), int(id_list.index(str(count))), -1):
        raw_email_string = get_need_msg(id_list[i], mail)
        q += 1
        print(q)

updcount(len(id_list), id_list[-1])

print(f"Прибыль: {analytics()}")