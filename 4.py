# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt, в одной строке одно число.

# Программа примет число N, создаст список соответствующей длины, заполнив его случайными числами от -N до N.
# Затем прочитает файл и перемножит числа, стоящие на соответствующей позиции в списке, если номер позиции корректный, т.е. число 7 в файле будет проигнорировано для списка из 5-ти элементов.

import random

def get_num_list (n):
    user_list = []
    while len(user_list) < n:
        user_list.append(random.randint(-n, n))
    return user_list

def get_mult_result (user_list):
    mult_result = 1
    f = open('file.txt')
    for line in f:
        index = int(line)
        if index > -1 and index < n:
            mult_result = mult_result * user_list[index]
    return mult_result


n = int(input('Введите число N: '))
list_to_multiply = get_num_list(n)
print(f'Сгенерирован список: {list_to_multiply}')
result = get_mult_result(list_to_multiply)
print(f'Результат перемножения элементов списка по допустимым индексам из файла: {result}')