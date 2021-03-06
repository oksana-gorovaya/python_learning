"""Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные
значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного
 списка"""


def find_odd(l):
    temp_list = []

    for item in l:
        if (item % 2 == 1) or (item == 0):
            temp_list.append(item)
        elif item % 2 == 0:
            continue
    return temp_list


def remove_odd(temp_list):
    for item in temp_list:
        if item in lst:
            lst.remove(item)
    return lst


def divide_by_half(lst):
    counter = 0
    for item in lst:
        lst[counter] = item // 2
        counter += 1
    return lst


def modify_list(lst):
    odd_numbers = find_odd(lst)
    filtered_list = remove_odd(odd_numbers)
    divide_by_half(filtered_list)


lst = [3, 2, 5, 5, -6, 0]
modify_list(lst)
print(lst)