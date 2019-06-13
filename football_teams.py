"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков"""
import re
games_total = int(input())
initial_table = []

while len(initial_table) < games_total:
    another_game = input()
    initial_table.append(another_game)


def create_match_table_template(initial_table):
    games_dictionary = {}

    for item in initial_table:
        for element in item.split(';'):
            if re.match("[а-яА-Я]", element):
                games_dictionary[element] = {'games_played': 0, 'won': 0, 'drawn': 0, 'lost': 0, 'points': 0}

    return games_dictionary


def preprocess_table_data(initial_table):
    arr = []
    for item in initial_table:
        arr.append(item.split(";"))
    for item in arr:
        keys_array = []
        values_array = []
        for element in item:
            if re.match("[а-яА-Я]", element):
                keys_array.append(element)
            else:
                values_array.append(element)
        temp_dictionary = dict(zip(keys_array, values_array))
        update_match_table(temp_dictionary, keys_array, values_array)


def update_match_table(temp_dictionary, keys_array, values_array):

    for key, value in temp_dictionary.items():
        match_table[key]['games_played'] += 1

        if value == values_array[0] == values_array[1]:
            match_table[key]['drawn'] += 1
            match_table[key]['points'] += 1

        elif value == max(values_array):
            match_table[key]['won'] += 1
            match_table[key]['points'] += 3

        else:
            match_table[key]['lost'] += 1


def format_results(match_table):
    output = ''
    for key, value in match_table.items():
        output += '\n' + key + ':'
        for values in value.values():
            output += str(values) + ' '
    return output


match_table = create_match_table_template(initial_table)
preprocess_table_data(initial_table)
print(format_results(match_table))