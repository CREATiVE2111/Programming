import json

data = [
    {   '_id': 1,
        'surname': 'Букаев',
        'name': 'Кирилл',
        'patronymic': 'Андреевич',
        'balance': 15000,
    },
    {
        '_id': 2,
        'surname': 'Иванов',
        'name': 'Иван',
        'patronymic': 'Иванович',
        'balance': 11000,

    },
    {
        '_id': 3,
        'surname': 'Самуйлов',
        'name': 'Игорь',
        'patronymic': 'Николаевич',
        'balance': 1000,
    },
    {
        '_id': 4,
        'surname': 'Климов',
        'name': 'Даня',
        'patronymic': 'Алексеевич',
        'balance': 20000,
    },
    {
        '_id': 5,
        'surname': 'Тарасенко',
        'name': 'Дарья',
        'patronymic': 'Дмитриевна',
        'balance': 50000,
    },
]
with open('client.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)


