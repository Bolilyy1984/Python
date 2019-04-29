# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

quoter_1_profit = dict([input('Введите прибыль за 1 кв фирм a, b и c (ключ - название компании): ').split() for _ in range(3)])
quoter_2_profit = dict([input('Введите прибыль за 2 кв фирм a, b и c (ключ - название компании): ').split() for _ in range(3)])
quoter_3_profit = dict([input('Введите прибыль за 3 кв фирм a, b и c (ключ - название компании): ').split() for _ in range(3)])
quoter_4_profit = dict([input('Введите прибыль за 4 кв фирм a, b и c (ключ - название компании): ').split() for _ in range(3)])

annual_profit_a = (float(quoter_1_profit['a']) + float(quoter_2_profit['a']) + float(quoter_3_profit['a']) + float(quoter_4_profit['a']))
annual_profit_b = (float(quoter_1_profit['b']) + float(quoter_2_profit['b']) + float(quoter_3_profit['b']) + float(quoter_4_profit['b']))
annual_profit_c = (float(quoter_1_profit['c']) + float(quoter_2_profit['c']) + float(quoter_3_profit['c']) + float(quoter_4_profit['c']))
annual_profit_all = annual_profit_a + annual_profit_b + annual_profit_c
annual_average_all = (annual_profit_all) // 3
print(f'Средняя прибыль за год по всем предприятиям составила {annual_average_all} млн. руб.')

if annual_profit_a > annual_average_all:
    print(f'Прибыль предприятия а оказалась выше среднегодовой и составила: {annual_profit_a}')
else:
    print(f'Прибыль предприятия а оказалась ниже среднегодовой и составила: {annual_profit_a}')

if annual_profit_b > annual_average_all:
    print(f'Прибыль предприятия b оказалась выше среднегодовой и составила: {annual_profit_b}')
else:
    print(f'Прибыль предприятия b оказалась ниже среднегодовой и составила: {annual_profit_b}')

if annual_profit_c > annual_average_all:
    print(f'Прибыль предприятия c оказалась выше среднегодовой и составила: {annual_profit_c}')
else:
    print(f'Прибыль предприятия c оказалась ниже среднегодовой и составила: {annual_profit_c}')