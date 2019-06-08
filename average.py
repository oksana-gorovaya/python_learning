"""" Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее
арифметическое всех чисел из отрезка [a;b], которые делятся на 3.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12]. Всего чисел, делящихся на 3,
на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.﻿"""

first_number = input()
second_number = input()

try:
    checking_first_input = int(first_number)
    checking_second_input = int(second_number)
except ValueError:
    print("Enter numbers only")


def calculate_average(first_number, second_number):
    counter = 0
    numbers_sum = 0
    for i in range(int(first_number), int(second_number) + 1):
        if i % 3 == 0:
            numbers_sum += i
            counter += 1
        continue

    return numbers_sum / counter


print(calculate_average(first_number, second_number))

