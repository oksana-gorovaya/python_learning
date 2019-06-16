"""Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
(программа не должна зависеть от регистра вводимых символов).

Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10⋅100=40.0, где 4 -- это количество
символов G и C,  а 10 -- это длина строки."""

string_to_check = input().lower()


def calculate_gc():
    counter = 0
    for i in string_to_check:
        if i == 'g' or i == 'c':
            counter += 1

    return counter / len(string_to_check) * 100


print(calculate_gc())
