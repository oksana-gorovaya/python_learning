"""Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. ﻿﻿"""

user_input = input().split()
input_sum = 0

for item in user_input:
    input_sum += int(item)

print(input_sum)
