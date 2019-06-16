"""Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. ﻿﻿"""

user_input = input().split()
input_sum = 0


def show_sum(user_input, input_sum):
    for item in user_input:
        input_sum += int(item)

    return input_sum


print(show_sum(user_input, input_sum))
