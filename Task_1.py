# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

my_list_1 = []
for _ in range(int(input('Введите длину списка 1: '))):
    my_list_1.append(random.randint(1, 21))

my_list_2 = []
for _ in range(int(input('Введите длину списка 2: '))):
    my_list_2.append(random.randint(1, 21))

print(my_list_1)
print(my_list_2)
final_list = []

for i in my_list_1:
    for j in my_list_2:
        if i == j:
            final_list.append(i)

print(set(final_list))

# final_list = list(set(my_list_1) & set(my_list_2)) -  можно такой вариант вместо циклов for, тогда
#                                                       печать без set
