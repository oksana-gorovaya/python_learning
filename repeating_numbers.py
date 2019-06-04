"""Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным."""
user_input = input().split(" ")
user_output = ""


def show_repeating_numbers(user_input, user_output):
    for item in user_input:
        if (user_input.count(item) > 1) and (item not in user_output.split(" ")):
            user_output += f"{item} "
        else:
            continue
    return user_output


print(show_repeating_numbers(user_input, user_output))
