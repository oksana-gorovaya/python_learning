"""Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11
включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего
требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
 Если про какой-то класс нет информации, необходимо вывести напротив него прочерк"""
import re

with open(input('Path to dataset file: '), 'r') as student_file:
    student_list = student_file.readlines()


def create_template():
    students_template = {}
    for item in range(1, 12):
        students_template[item] = '-'

    return students_template


def get_height(student_list):
    trimmed_list = []
    height_list = []
    for item in student_list:
        trimmed_list.append(item.strip().split('\t'))

    for item in trimmed_list:
        form_number = []
        student_height = []
        for element in item:
            if re.match("[0-9]", element):
                if int(element) <= 11:
                    form_number.append(int(element))
                else:
                    student_height.append(element)
        height_list.append(dict(zip(form_number, student_height)))

    return height_list


def fill_template(output_template, student_height_list):
    counter = []

    for item in student_height_list:
        key = list(item)[0]
        value = item.get(key)

        if output_template[int(key)] == '-':
            output_template[int(key)] = int(value)
        else:
            output_template[int(key)] += int(value)
        counter.append(int(key))

    for key, value in output_template.items():
        if value != '-':
            output_template[key] = value / counter.count(key)

    return output_template


def format_output(output):
    string_output = ''
    splitted_output = str(output).split(',')
    for item in splitted_output:
        string_output += item.split(':')[0] + ' ' + item.split(':')[1] + '\n'

    final_output = string_output.replace('{', ' ').replace('}', ' ')

    return final_output


output_template = create_template()
student_height_list = get_height(student_list)
output = fill_template(output_template, student_height_list)
formatted_output = format_output(output)

with open(input('Path to output file: '), 'w') as output_file:
    output_file.write(formatted_output)
