'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
'''
import cProfile


def sieve(num,pos):
    prime = [True for i in range(num + 1)]
    p = 2
    num_list = []
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * 2, num + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(num + 1):
        if prime[p]:
            num_list.append(p)
    return num_list[pos-1]

# 100 loops, best of 5: 4.56 usec per loop "les_4_task_2.sieve(10,3)"
# 100 loops, best of 5: 18.9 usec per loop "les_4_task_2.sieve(100,10)"
# 100 loops, best of 5: 17.4 usec per loop "les_4_task_2.sieve(100,25)"
# 100 loops, best of 5: 231 usec per loop "les_4_task_2.sieve(1000,100)"
# 100 loops, best of 5: 1.91 msec per loop "les_4_task_2.sieve(10000,200)"

# cProfile.run('sieve(10,3)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:10(sieve)
# cProfile.run('sieve(100,10)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:10(sieve)
# cProfile.run('sieve(100,25)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:10(sieve)
# cProfile.run('sieve(1000,100)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:10(sieve)
# cProfile.run('sieve(10000,200)')
# 1    0.005    0.005    0.007    0.007 les_4_task_2.py:10(sieve)


def prime(num):
    count = 1
    number = 1
    prime = [2]

    if num == 1:
        return 2

    while count != num:
        number += 2
        for i in prime:
            if number % i == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

# 100 loops, best of 5: 811 nsec per loop "les_4_task_2.sieve(3)"
# 100 loops, best of 5: 14 usec per loop "les_4_task_2.sieve(10)"
# 100 loops, best of 5: 26.8 usec per loop "les_4_task_2.sieve(25)"
# 100 loops, best of 5: 549 usec per loop "les_4_task_2.sieve(100)"
# 100 loops, best of 5: 1.23 msec per loop "les_4_task_2.sieve(200)"

# cProfile.run('prime(3)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:44(prime)
# cProfile.run('prime(10)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:44(prime)
# cProfile.run('prime(25)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:44(prime)
cProfile.run('prime(100)')
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:44(prime)
# cProfile.run('prime(200)')
# 1    0.003    0.003    0.003    0.003 les_4_task_2.py:44(prime)
