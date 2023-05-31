import datetime
import tabulate
import pymongo
import json

cluster = pymongo.MongoClient("mongodb://91.190.239.132:27027")
db = cluster["shad112_v3"]
client = db["client"]
products = db["products"]
refill_sell = db["refill_sell"]
# 1--------------------------------------------------------------------------------------------------------------------

# 2--------------------------------------------------------------------------------------------------------------------
def add_client(id, surname, name, patronymic, balance):
    try:
        client.insert_one({'_id': id, 'surname': surname, 'name': name, 'patronymic': patronymic, 'balance': balance})
    except pymongo.errors.DuplicateKeyError:
        print(f'ERROR: Клиент с таким id ({id}) уже существует')
    else:
        print(f"Добавлен клиент: {surname} {name} {patronymic}. Его баланс {balance}")

def change_client(id, param, change):
    data = client.find_one({'_id': id})
    try: data['name']
    except TypeError:
        print(f'ERROR: Клиента с таким id ({id}) не существует')
    else:
        products.update_one({'_id': id}, {"$set": {param: change}})
        print(f"У клиента {data['surname']} {data['name']} {data['patronymic']} изменён параметр {param}. Новое значение {change}")
def find_client(id, param, change):
    data = client.find_one({'_id':  id})
    try: data['name']
    except TypeError:
        print(f'ERROR: Клиента с таким id ({id}) не существует')
    else:
        products.update_one({'_id': id}, {"$set": {param: change}})
        print(f"У клиента {data['surname']} {data['name']} {data['patronymic']} изменён параметр {param}. Новое значение {change}")

def delet_client(id):
    data = client.find_one({'_id': id})
    try: data['name']
    except TypeError:
        print(f'Клиент с таким id ({id}) не найден')
    else:
        client.delete_one({'_id': id})
        print(f"Удалён клиент {data['surname']} {data['name']} {data['patronymic']}")

def add_product(id, name, count, price, min_count):
    try:
        products.insert_one({'_id': id, 'name': name, 'count': count, 'price': price, 'min_count': min_count})
    except pymongo.errors.DuplicateKeyError:
        print(f"ERROR: Товар с таким id ({id}) уже существует")
    else:
        print(f"Добавлен подукт: {name} c id: {id}, в количестве: {count}, с ценой: {price}, и минимальным запасом: {min_count}")

def change_product(id, param, change):
    data = products.find_one({'_id': id})
    try: data['name']
    except TypeError:
        print(f'ERROR: Товар с таким id ({id}) не существует')
    else:
        products.update_one({'_id': id}, {"$set": {param: change}})
        print(f"Параметр {param} продукта '{data['name']}' был изменён. Новое значение: {change}")

def delet_product(id):
    data = products.find_one({'_id': id})
    try: data['name']
    except TypeError:
        print(f'Товар с таким id ({id}) не найден')
    else:
        products.delete_one({'_id': id})
        print(f"Удалён продукт '{data['name']}'")
# 3--------------------------------------------------------------------------------------------------------------------
def initDB():
    clear_collections()
    start_insert_client('client.json')
    start_insert_products('products.json')
    print('Коллекции созданы')

def clear_collections():
    client.drop()
    products.drop()
    refill_sell.drop()
    print('Коллекции удалены')

def start_insert_client(file):
    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
        # client.insert_many(data)
        for infOne in data:
            add_client(infOne['_id'], infOne['surname'], infOne['name'], infOne['patronymic'], infOne['balance'])
            print(f'Добавлены значения {infOne}')

def start_insert_products(file):
    with open(file, "r", encoding='utf-8') as file:
        data = json.load(file)
        for d in data:
            add_product(d['_id'], d['name'], d['count'], d['price'], d['min_count'])
            print(f'Добавлены значения {d}')
# 4--------------------------------------------------------------------------------------------------------------------
def refill_product(id, count, date):
    data = products.find_one({'_id': id})
    try: data['name']
    except TypeError:
        print(f'Продукта с таким id ({id}) не существует')
    else:
        products.update_one({'_id': id}, {"$inc": {'count': count}})
        print(f"Запас продукта '{data['name']}' был пополнен на {count}")
        add2refill_sell(data['name'], "Пополнение", date, count, data['price'])

def sell_product(id, count):
    data = products.find_one({'_id': id})
    try: data['count']
    except TypeError:
        print(f'Продукта с таким id ({id}) не существует')
        return 'error'
    else:
        if ((data['count'] - count) >= 0) and ((data['count'] - count) >= data['min_count']):
            products.update_one({'_id': id}, {"$inc": {'count': -count}})
            print(f"Продукт '{data['name']}' был продан в количестве: {count}")
            return data['price'] * count
        elif ((data['count'] - count) >= 0) and ((data['count'] - count) <= data['min_count']):
            products.update_one({'_id': id}, {"$inc": {'count': -count}})
            print(f"Продукт '{data['name']}' был продан в количестве: {count}")
            print(f"Внимание! Запас товара меньше минимального на {data['min_count'] - (data['count'] - count)}")
            return data['price'] * count
        else:
            print(F"Невозможно продать продукт '{data['name']}'. Не хватает количества")
            return 'error'

def refill_balance(id, count):
    data = client.find_one({'_id': id})
    try: data['balance']
    except TypeError:
        print(f'Клиента с таким id ({id}) не существует')
    else:
        client.update_one({'_id': id}, {'$inc': {'balance': count}})
        print(f'{data["surname"]} {data["name"]} пополнил баланс на сумму {count}')

def withdraw_balance(id, count):
    data = client.find_one({'_id': id})
    try: data['balance']
    except TypeError:
        print(f'Клиента с таким id ({id}) не существует')
        return 'error'
    else:
        if (data['balance'] - count) >= 0:
            client.update_one({'_id': id}, {'$inc': {'balance': -count}})
            print(f'С баланса {data["surname"]} {data["name"]} списано {count}')
        else:
            print(f'Невозможно списать средства с баланса {data["surname"]} {data["name"]}. Недостаточно средств')
            return 'error'
# 5--------------------------------------------------------------------------------------------------------------------
def makeJob():
    add_product(12, "Коврик", 10, 150, 3)
    add_product(12, "Коврик", 10, 150, 3)
    add_product(11, "Салфетки", 10, 5, 20)
    print()
    change_product(2, 'name', 'Игрушечный мяч v2.0')
    change_product(22, 'name', 'Игрушечный мяч v2.0')
    print()
    delet_product(3)
    delet_product(3)
    print()
    add_client(10, 'Василев', 'Алексей', 'Иванович', 22111)
    add_client(10, 'Василев', 'Алексей', 'Иванович', 22111)
    print()
    change_client(2, 'balans', 5768)
    change_client(222, 'balans', 5768)
    print()
    delet_client(3)
    delet_client(3)
    print()
    refill_product(1, 1, '10-05-2023')
    refill_product(123, 1, '10-05-2023')
    print()
    sell_product(1, 1)
    sell_product(1, 3245)
    sell_product(4, 3)
    sell_product(134, 1)
    print()
    refill_balance(1, 5)
    refill_balance(145, 5)
    print()
    withdraw_balance(2, 5)
    withdraw_balance(2, 999999)
    withdraw_balance(267, 5)
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    make_order(1, 1, 4, '11-05-2023')
    make_order(1, 1, 4, '11-05-2023')
    refill_product(1, 10, '11-05-2023')
    make_order(2, 1, 4, '12-05-2023')
    make_order(3, 1, 4, '13-05-2023')
    make_order(1, 2, 4, '14-05-2023')
    make_order(1, 3, 4, '15-05-2023')
    make_order(1, 4, 123, '16-05-2023')
    make_order(5, 4, 2, '17-05-2023')
    refill_product(6, 7, '17-05-2023')
    make_order(5, 5, 2, '18-05-2023')
    make_order(5, 6, 2, '19-05-2023')
    make_order(5, 7, 2, '20-05-2023')
    make_order(5, 8, 2, '21-05-2023')
    refill_product(2, 10, '21-05-2023')
    make_order(5, 2, 2, '21-05-2023')
    make_order(10, 11, 30, '23-05-2023')

def make_order(client, product, count, date):
    cash = sell_product(product, count)
    if cash == 'error': pass
    else:
        exc = withdraw_balance(client, cash)
        if exc: pass
        else:
            add2refill_sell(product, client, date, count, cash)

# 6--------------------------------------------------------------------------------------------------------------------
def add2refill_sell(name, operation, date, count, price):
    data = client.find_one({'_id': operation}, {'surname': True, 'name': True, 'patronymic': True})
    pdata = products.find_one({'_id': name}, {'name': True})
    date = date.split('-')
    date = list(map(int, date))
    d, m, y = date
    if operation == 'Пополнение':
        refill_sell.insert_one({'name': name, 'operation': operation, 'date': datetime.datetime(y, m, d),
                                'count': count, 'price': price})
    elif operation == 'error':
        pass
    else:
        refill_sell.insert_one({'name': pdata['name'], 'operation': data['surname'] + ' ' +  data['name'] + ' ' +
                                data['patronymic'], 'date': datetime.datetime(y, m, d), 'count': count, 'price': price})

def stat1(start_date, end_date):
    data = refill_sell.find().sort([('date', 1), ('name', 1)])
    table = [['Дата', 'Название', 'Покупатель/пополнение', 'Колличество', 'Цена\nпроверка']]
    for d in data:
        if str(d['date']) >= start_date and str(d['date']) <= end_date:
            table.append([d['date'], d['name'], d['operation'], d['count'], d['price']])
    print(tabulate.tabulate(table, tablefmt="grid", stralign='center'))

def stat2(start_date, end_date):
    bs = []
    ba = []
    data = refill_sell.find().sort([('name', 1)])
    table = [['Название', 'Поступило', 'Продано', 'Сумма продаж', 'Покупатель']]
    for d in data:
        if str(d['date']) >= start_date and str(d['date']) <= end_date:
            if d['name'] not in bs and d['operation'] != 'Пополнение':
                bs.append(d['name'])
                bs.append(d['count'])
                bs.append([d['operation']])
                bs.append(d['price'])
            elif d['name'] in bs and d['operation'] != 'Пополнение':
                bs[bs.index(d['name']) + 1] = bs[bs.index(d['name']) + 1] + d['count']
                bs[bs.index(d['name']) + 3] = bs[bs.index(d['name']) + 3] + d['price']
                if d['operation'] not in bs[bs.index(d['name']) + 2]:
                    bs[bs.index(d['name']) + 2].append(d['operation'])
            if d['name'] not in ba and d['operation'] == 'Пополнение':
                ba.append(d['name'])
                ba.append(d['count'])
            elif d['name'] in ba and d['operation'] == 'Пополнение':
                ba[ba.index(d['name']) + 1] = ba[ba.index(d['name']) + 1] + d['count']
    for i in range(2, len(bs), 4):
        buyers = str()
        if len(bs[i]) > 1:
            for j in bs[i]:
                buyers = f"{buyers}{j}\n"
            bs[i] = buyers[0:-1]
        else:
            bs[i] = str(bs[i][0])
    for i in range(0, len(bs), 4):
        table.append([bs[i], 0, bs[i+1], bs[i+3], bs[i+2]])
    for i in range(0, len(ba), 2):
        for j in range(len(table)):
            if ba[i] in table[j]:
                table[j][table[j].index(ba[i]) + 1] = ba[i + 1]
    print(tabulate.tabulate(table, tablefmt="grid", stralign='center'))
def stat3(date):
    data = products.find()
    table = [['Название', 'Минимальный\nостаток', 'Текущий\nостаток', 'Заказано\nна дату', 'Необходимая\nпоставка']]
    for d in data:
        if d['count'] - d['min_count'] <= 0:
            table.append([d['name'], d['min_count'], d['count'], '-', d['min_count'] - d['count']])
        else:
            table.append([d['name'], d['min_count'], d['count'], '-', 0])
    print(tabulate.tabulate(table, tablefmt="grid", stralign='center'))

initDB()
print('\n\n')
makeJob()
stat1('2023-05-10 00:00:00', '2023-05-21 00:00:00')
print('\n\n')
stat2('2023-05-10 00:00:00', '2023-05-21 00:00:00')
print('\n\n')
stat3('23-05-2023')