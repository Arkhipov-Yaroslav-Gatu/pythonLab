# Задание 1. Напишите программу.


"""
Пользователь вводит натуральное число n.
Программа в ответ выводит на экран список из n случайных целых чисел из диапазона [0; 100].
"""

from random import randint

n = int(input("Введите число"))

for i in range(n):
    print(randint(0, 100))