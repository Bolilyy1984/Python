# Задача №1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

int_num = int(input('Введите трехзначное число: '))
num_a = int_num % 10
int_num = int_num // 10
num_b = int_num % 10
num_c = int_num // 10
print(f'Сумма цифр трехзначного числа: {num_a + num_b + num_c}')
print(f'Произведение цифр трехзначного числа: {num_a * num_b * num_c}')

# Задача №9
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)

# Задача №3
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
print('Введите координаты точек A и B: ')
x1 = float(input('точка А: х1 = '))
y1 = float(input('точка А: y1 = '))
x2 = float(input('точка B: х2 = '))
y2 = float(input('точка B: y2 = '))

# Вычисление введенных данных для подстановки в уравнение y=kx+b
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f'Переменная вида y=kx+b по введенным координатам: y = {k}x + {b}')

# Задача №5
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

rus_alph = ['а', 'б', 'в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш',
           'щ','ъ','ы','ь','э','ю','я']
lit_1 = input('Введите русскую букву 1:')
lit_2 = input('Введите русскую букву 2:')
number_1 = rus_alph.index(lit_1) + 1
number_2 = rus_alph.index(lit_2) + 1
amount_lit = abs(number_1 - number_2) - 1
print(f'Номера введенных букв в алфавите: {number_1}, {number_2}, между ними {amount_lit} букв(ы)')

# Задача №2
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))
print("%d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))
print("%d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))
print("%d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
print("%d << 2 = %d (%s)" % (b, b << 2, bin(b << 2)))
print("%d >> 2 = %d (%s)" % (b, b >> 2, bin(b >> 2)))

# Задача 8
# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year_days = int(input('Введите количество дней в году: '))
if year_days % 4 != 0:
    print("Год - НЕвисокосный")
elif year_days % 100 == 0:
    if year_days % 400 == 0:
        print("Високосный")
    else:
        print("НЕвисокосный")
else:
    print("Високосный")
