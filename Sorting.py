import time
import random

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 10000
NUMBER_OF_TESTS = 5
RAND_MAX = 100000

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_
def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True
def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            #print("Required time in test №", test_number + 1, "is", timer, "seconds")
            ty=1
        else:
            print("Error in test №", test_number + 1)
    #print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")
def search_test(func):
    total_timer = 0
    test_list = sorted(generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST))
    for test_number in range(NUMBER_OF_TESTS):
        timer = time.time()
        search_elem = random.randint(-RAND_MAX, RAND_MAX)
        answer = func(test_list, search_elem)
        timer = time.time() - timer
        total_timer += timer
        if not(search_check(test_list, search_elem, answer)):
            print("Error in test №", test_number + 1)
    print("Total time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")
def search_check(list_, search_elem, answer):
    if answer == None:
        for index in range(len(list_)):
            if list_[index] == search_elem:
                return False
        return True
    else:
        if list_[answer] == search_elem:
            return True
        else:
            return False

def BubbleSort(array):
    swapped = True
    last_index = len(array)
    while swapped:
        swapped = False
        for index in range(last_index - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                swapped = True
        last_index -= 1
    return array
def selectionSort(array):
    for i in range(len(array) - 1):
        m = i
        for j in range(i + 1, len(array)):
            if array[j] < array[m]:
                m = j
        array[i], array[m] = array[m], array[i]
    return array
def insertion(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while array[j] > x and j >= 0 :
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x
    return array
def insertionBinary(array):
    for i in range(len(array)):
        key = array[i]
        start, end = 0, i - 1
        while start < end:
            mid = start + (end - start) // 2
            if key < array[mid]:
                end = mid
            else:
                start = mid + 1
        for j in range(i, start + 1, -1):
            array[j] = array[j - 1]
        array[start] = key
    return array
def mergeSort(array):
    if len(array) == 1:
        return array
    mid = (len(array) - 1) // 2
    left = mergeSort(array[:mid + 1])
    right = mergeSort(array[mid + 1:])
    result = merge(left, right)
    return result
def merge(left, right):
    lst = []
    i = 0
    j = 0
    while(i <= len(left) - 1 and j <= len(right) - 1):
        if left[i]<right[j]:
            lst.append(left[i])
            i+=1
        else:
            lst.append(right[j])
            j+=1
    if i>len(left)-1:
        while(j <= len(right) - 1):
            lst.append(right[j])
            j+=1
    else:
        while(i <= len(left) - 1):
            lst.append(left[i])
            i+=1
    return lst
def quick_sort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array = array[::-1]
        return array
    else:
        left = []
        right = []
        center = []
        elem = array[0]
        for i in array:
            if i < elem:
                left.append(i)
            elif i == elem:
                center.append(i)
            elif i > elem:
                right.append(i)
        return quick_sort(left) + center + quick_sort(right)
def PYsort(array):
    array.sort()
    return array

test(BubbleSort)
test(selectionSort)
test(insertion)
test(insertionBinary)
test(mergeSort)
test(quick_sort)
test(PYsort)
'''
Average time for 10 tests is 8.104839062690735 seconds
Average time for 10 tests is 3.0643253326416016 seconds
Average time for 10 tests is 3.5503326892852782 seconds
Average time for 10 tests is 1.9040141344070434 seconds
Average time for 10 tests is 0.03451130390167236 seconds
Average time for 10 tests is 0.015855693817138673 seconds
Average time for 10 tests is 0.0009961605072021484 seconds
'''