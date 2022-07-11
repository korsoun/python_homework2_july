# Реализуйте алгоритм перемешивания списка

import random

shuffled_list = [1, 2, 3, 4, 5, 6]

def shufflingLists (shuffled_list):
    shuffling_list = shuffled_list[:]
    random.shuffle(shuffling_list)
    return shuffling_list

print(f'Исходный список {shuffled_list}')
print(f'Перемешанный список {shufflingLists(shuffled_list)}')