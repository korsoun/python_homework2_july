# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4).

def get_multipled_list (n):
    function_list = []
    multiply = 1
    for i in range (1, n+1):
        multiply *= i 
        function_list.append(multiply)
    return function_list

n = int(input('Введите число N: '))
print(get_multipled_list(n))