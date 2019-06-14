"""Группа биологов в институте биоинформатики завела себе черепашку.
После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное
расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу, которая
определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, которая
выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение начинается
в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.

Программе подаётся на вход число команд n, которые нужно выполнить черепашке, после чего n строк с самими командами.
Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты
целочисленные."""
import re


def fill_dynamic_list(entries_number):
    filled_list = []
    while len(filled_list) < entries_number:
        another_entry = input().lower()
        filled_list.append(another_entry)

    return filled_list


instructions_number = int(input())
instructions = fill_dynamic_list(instructions_number)


def list_to_dictionary(instructions):
    splited_items = []
    instructions_array = []

    for item in instructions:
        splited_items.append(item.split(' '))

    for item in splited_items:
        instructions_keys = []
        instructions_values = []
        for element in item:
            if re.match("[0-9]", element):
                instructions_values.append(element)
            else:
                instructions_keys.append(element)

        instructions_array.append(dict(zip(instructions_keys, instructions_values)))

    return instructions_array


def get_directions(preprocessed_instructions):
    route = {'x': 0, 'y': 0}
    for item in preprocessed_instructions:
        for key, value in item.items():
            if key == 'север':
                route['y'] += int(value)
            elif key == 'запад':
                route['x'] -= int(value)
            elif key == 'юг':
                route['y'] -= int(value)
            elif key == 'восток':
                route['x'] += int(value)
            else:
                raise Exception('This tortoise supports Russian instructions only')

    return route


def format_output(finish_coordinates):
    output = ''
    for value in finish_coordinates.values():
        output += str(value) + ' '

    return output


preprocessed_instructions = list_to_dictionary(instructions)
finish_coordinates = get_directions(preprocessed_instructions)
formatted_output = format_output(finish_coordinates)
print(formatted_output)