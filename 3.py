# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

def get_series_list (n):
    series_list = []
    for i in range(1, n + 1):
        series_list.append(round((1 + 1/i)**i, 4))
    return series_list

def get_list_sum (entering_list):
    sum = 0
    for i in entering_list:
        sum = round(i + sum, 4)
    return sum

n = int(input('Введите количество чисел последовательности: '))
print(f'Ваш ряд: {get_series_list(n)}, сумма этого ряда: {round(get_list_sum(get_series_list(n)), 4)}') 