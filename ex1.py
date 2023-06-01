import os
def clear_console():
    os.system("cls")
clear_console()
import random

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input("Введи N: "))
res = []
for i in range(N):
    y = random.randint(1,11)
    res.append(y)
print(res)

Number = int(input("Введите искомое число: "))
count = 0
for j in range(N):
    if res[j] == Number:
        count += 1
print(f'Число {Number} встречается в массиве {count} раз.')