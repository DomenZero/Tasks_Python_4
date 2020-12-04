
"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Задача 4 из урока 3
Определить, какое число в массиве встречается чаще всего

"""

import random
import cProfile
# Решение 1
def detect(num):
    ln = len(num) - 1
    rate = []
    ch = 0
    first = num[0]
    k = 0
    max_am = 0
    max_ch = 0
    for i in range(ln):
        first = num[i]
        if num[i] == first and first != 'n':
            for i, item in enumerate(num[:]):
                if num[i] == first and num[i] != 'n':
                    ch += 1
                    num[i] = 'n'
            if max_am < ch:
                max_am = ch
                max_ch = first
            k += 1
            ch = 0

    return max_ch, max_am

# 100 loops, best of 5: 31.7 usec per loop "x = [random.randint(1, 10) for _ in range(10)]"
# 100 loops, best of 5: 23.7 usec per loop "x = [random.randint(1, 100) for _ in range(10)]"
# 100 loops, best of 5: 73.3 usec per loop "x = [random.randint(1, 1000) for _ in range(10)]"
# 100 loops, best of 5: 1.74 msec per loop "x = [random.randint(1, 1000) for _ in range(100)]"
# 100 loops, best of 5: 86.9 msec per loop "x = [random.randint(1, 1000) for _ in range(1000)]"
# x = [random.randint(1, 10) for _ in range(10)]
# x = [random.randint(1, 100) for _ in range(10)]
# x = [random.randint(1, 1000) for _ in range(10)]
# x = [random.randint(1, 1000) for _ in range(100)]
# 1    0.002    0.002    0.002    0.002 les_4_task_1.py:20(detect)
# x = [random.randint(1, 1000) for _ in range(1000)]
# 1    0.080    0.080    0.080    0.080 les_4_task_1.py:20(detect)
# cProfile.run('detect (x)')


# Решение 2
def detect2(num):
    u_num = {i: 0 for i in set(num)}
    for i in num:
        u_num[i] += 1

    max_x = 0
    for key, item in u_num.items():
        if item > max_x:
            max_ch = key
            max_x = item
    return max_ch

# 100 loops, best of 5: 13.2 usec per loop "x = [random.randint(1, 10) for _ in range(10)]"
# 100 loops, best of 5: 13.7 usec per loop "x = [random.randint(1, 100) for _ in range(10)]"
# 100 loops, best of 5: 19.3 usec per loop "x = [random.randint(1, 1000) for _ in range(10)]"
# 100 loops, best of 5: 213 usec per loop loop "x = [random.randint(1, 1000) for _ in range(100)]"
# 100 loops, best of 5: 1.47 msec per loop "x = [random.randint(1, 1000) for _ in range(1000)]"
# x = [random.randint(1, 10) for _ in range(10)]
# x = [random.randint(1, 100) for _ in range(10)]
# x = [random.randint(1, 1000) for _ in range(10)]
# x = [random.randint(1, 1000) for _ in range(100)]
# x = [random.randint(1, 1000) for _ in range(1000)]
# 1    0.000    0.000    0.001    0.001 les_4_task_1.py:61(detect2)
# cProfile.run('detect2 (x)')

# ***** Результат detect2 лучше по времени чем у detect и по скорости тоже

# Решение 3
def detect3(num):
    dict = {}
    for item in num:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 1
    result = max(dict, key=lambda k: dict[k])
    return result

# 100 loops, best of 5: 42.2 usec per loop "x = [random.randint(1, 10) for _ in range(10)]"
# 100 loops, best of 5: 23.6 usec per loop "x = [random.randint(1, 100) for _ in range(10)]"
# 100 loops, best of 5: 222 usec per loop "x = [random.randint(1, 1000) for _ in range(10)]"
# 100 loops, best of 5: 30 usec per loop "x = [random.randint(1, 1000) for _ in range(100)]"
# 100 loops, best of 5: 1.42 msec per loop "x = [random.randint(1, 1000) for _ in range(1000)]"
# x = [random.randint(1, 10) for _ in range(10)]
# x = [random.randint(1, 100) for _ in range(10)]
# x = [random.randint(1, 1000) for _ in range(10)]
# x = [random.randint(1, 1000) for _ in range(100)]
# x = [random.randint(1, 1000) for _ in range(1000)]
# 1    0.000    0.000    0.001    0.001 les_4_task_1.py:87(detect3)
#       637    0.000    0.000    0.000    0.000 les_4_task_1.py:94(<lambda>)
# cProfile.run('detect3 (x)')

#  ***** использование словаря в два раза быстрее чем detect2