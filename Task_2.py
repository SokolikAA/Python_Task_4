# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом
# кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9

import random

my_list = []
num_bushes = int(input('Введите количество кустов: '))
for _ in range(num_bushes):
    my_list.append(random.randint(1, 10))
print(f'{num_bushes} -> {my_list}')
sum_berry = 0
if sum_berry <= (my_list[- 1] + my_list[0] + my_list[1]):
    sum_berry = (my_list[- 1] + my_list[0] + my_list[1])
if sum_berry <= (my_list[num_bushes-2] + my_list[num_bushes-1] + my_list[0]):
    sum_berry = (my_list[num_bushes-2] + my_list[num_bushes-1] + my_list[0])
for i in range(1, len(my_list)-2):
    if sum_berry <= (my_list[i-1] + my_list[i] + my_list[i+1]):
        sum_berry = (my_list[i-1] + my_list[i] + my_list[i+1])
print(f' максимального числа ягод, которое может собрать за один заход собирающий модуль - {sum_berry} ')
