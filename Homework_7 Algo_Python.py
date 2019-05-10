
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

# Метод пузырька

import timeit
import random

def bubble_sort(array):
    a = array
    for k in range(len(a) - 1, 0, -1):
        for i in range(k):
            if a[i] < a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
        # print(a)

numbers = [random.randint(-100,100) for i in range(20)]


print('Исходный массив:', numbers)
bubble_sort(numbers)
print('Отсортированный массив:', numbers)

# Быстрая сортировка

def quick_sort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] > pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]

        first_part = quick_sort(x[:i])
        second_part = quick_sort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part

print('Первоначальный массив:', numbers)
quick_sort(numbers)
print('Исходный массив:', numbers)
