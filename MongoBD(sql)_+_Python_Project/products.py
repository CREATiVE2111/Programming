import json

data = [
    {
        '_id': 1,
        'name': 'Вискас',
        'count': 10,
        'price': 20,
        'min_count': 10
    },
    {
        '_id': 2,
        'name': 'Игрушечный мяч',
        'count': 5,
        'price': 50,
        'min_count': 10
    },
    {
        '_id': 3,
        'name': 'Корм сухой для котов',
        'count': 7,
        'price': 149,
        'min_count': 9
    },
    {
        '_id': 4,
        'name': 'Корм сухой для кошек',
        'count': 8,
        'price': 149,
        'min_count': 7
    },
    {
        '_id': 5,
        'name': 'Корм сухой для собак',
        'count': 9,
        'price': 149,
        'min_count': 7
    },
    {
        '_id': 6,
        'name': 'Консервированный корм для котов',
        'count': 9,
        'price': 79,
        'min_count': 7
    },
    {
        '_id': 7,
        'name': 'Консервированный корм для кошек',
        'count': 8,
        'price': 79,
        'min_count': 8
    },
    {
        '_id': 8,
        'name': 'Консервированный корм для собак',
        'count': 7,
        'price': 79,
        'min_count': 9
    },
    {
        '_id': 9,
        'name': 'Шампунь для собак и кошек всех пород',
        'count': 10,
        'price': 249,
        'min_count': 8
    },
    {
        '_id': 10,
        'name': 'Корм для попугаев',
        'count': 10,
        'price': 179,
        'min_count': 7
    },
]

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
