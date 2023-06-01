import os
def clear_console():
    os.system("cls")
clear_console()
import random
# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("Введи N: "))
res = []
for i in range(N):
    y = random.randint(1,1001)
    res.append(y)
print(res)
Number = int(input("Введите искомое число: "))

min = (res[0] - Number)
index = 0


for j in range(N):
    delta = (res[j] - Number)
    if delta < min:
        min = delta
        index = j
print(f'Число {res[index]} ближе всего к числу {Number}')

