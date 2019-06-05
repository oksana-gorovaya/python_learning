"""Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна вывести
фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].

Числа a, b, c и d являются натуральными и не превосходят 10, a<=b, c<=d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и
строка таблицы."""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
args = [a, b, c, d]


def build_header():
    range_string = ''
    for f in range(c, d + 1):
        range_string += '\t' + str(f)
    return range_string


for item in args:
    if (item == 0) or (item >= 10):
        raise Exception("Enter integers from 0 to 9")
    elif (a > b) or (c > d):
        raise Exception("Use the following format: a<=b, c<=d")

print(build_header())


def build_table():
    string_to_fill = ''
    result = ''
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            string_to_fill += str(j * i) + '\t'
        result += f'{i}\t{string_to_fill}\n'
        string_to_fill = ''
    return result


print(build_table())
