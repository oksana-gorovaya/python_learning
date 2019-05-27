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

range_string = ''
string_to_fill = ''

for f in range(c, d + 1):
    range_string += '\t' + str(f)

print(range_string)

for i in range(a, b + 1):
    for j in range(c, d + 1):
        string_to_fill += str(j * i) + '\t'
    print(f'{i} \t {string_to_fill}')
    string_to_fill = ''


