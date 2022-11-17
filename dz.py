import random

RAND_MAX = 100000

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    print(list_)
    return list_


def select(list_):
    for i in range(len(list_)):
        minimum = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[minimum]:
                minimum = j
        list_[minimum], list_[i] = list_[i], list_[minimum]

    return list_

def insert(list_):
    for i in range(len(list_)):
        j = i - 1
        key = list_[i]
        while list_[j] > key and j >= 0:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key
    print(list_)
    return list_

def insert_bin(list_):
    for i in range(len(list_)):
        k = list_[i]
        x, y = 0, i - 1
        while x < y:
            m = x + (y - x) // 2
            if k < list_[m]:
                y = m
            else:
                x = m + 1
        for j in range(i, x + 1, -1):
            list_[j] = list_[j - 1]
        list_[x] = k
    print(list_)
    return list_

select(generate_list(100))
insert(generate_list(100))
insert_bin(generate_list(100))