
# Задача №1 для сранения:
# В одномерном массиве целых чисел определить два наименьших элемента.
# Одни могут быть как равны между собой (оба являться минимальными), так и различаться.


import timeit
import random

size = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

# var #1
def without_remove():
    min_first, min_second = (0, 1) if array[0] > array[1] else (1, 0)
    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam
            elif array[i] < array[min_second]:
                min_second = i
    # print(f'Число {array[min_first]} в ячейке {min_first}')
    # print(f'Число {array[min_second]} в ячейке {min_second}')

without_remove()

# var #1 с удалением
def with_remove():
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)
    print(min_1, min_2)

with_remove()

print(timeit.timeit("without_remove()", setup="from __main__ import without_remove", number=100000))
print(timeit.timeit("with_remove()", setup="from __main__ import with_remove", number=100000))


# Задача №2 для сравнения:
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def reverse_algo():
    n = 123456789
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n = n//10
    print(m)
reverse_algo()

def reverse_slice():
    n = 123456789
    m = (n[::-1])
    print(m)
reverse_slice()

print(timeit.timeit("reverse_algo()", setup="from __main__ import reverse_algo", number=100000))
print(timeit.timeit("reverse_slice()", setup="from __main__ import reverse_slice", number=100000))