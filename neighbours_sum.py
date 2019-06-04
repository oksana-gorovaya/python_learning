"""Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого
списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход
ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом."""

user_input = input().split(" ")
user_output = ""
counter = 0


def show_neighbours_sum(user_input, user_output, counter):
    if len(user_input) == 1:
        user_output += str(user_input[0])

    else:
        for item in user_input:
            neighbours_sum = 0
            if counter == 0:
                neighbours_sum = int(user_input[1]) + int(user_input[-1])

            elif counter == (len(user_input) - 1):
                neighbours_sum = int(user_input[-2]) + int(user_input[0])

            else:
                neighbours_sum = int(user_input[counter + 1]) + int(user_input[counter - 1])

            user_output += str(neighbours_sum) + " "
            counter += 1
    return user_output


print(show_neighbours_sum(user_input, user_output, counter))
