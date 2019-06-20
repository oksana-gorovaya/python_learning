"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку
по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по
всем абитуриентам:
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']"""
input_file = input()
output_file = input()


def separate_students(input_data):
    students_list = []
    for item in input_data:
        students_list.append(item.split(";"))
    return remove_name(students_list)


def remove_name(students_list):
    for item in students_list:
        del item[0]
    return students_list


def find_average_grade(students_grades_list):
    arr = []
    counter = 0
    for item in students_grades_list:
        grades = 0
        for element in item:
            grades += float(element)
            counter = len(item)
        average = grades / counter
        arr.append(f"{round(average, 11)}\n")
    return "".join(arr)


def find_average_per_subject(students_grades_list):
    math_grades = []
    physics_grades = []
    language_grades = []
    for item in students_grades_list:
        for element in item:
            math_grades.append(float(item[0]))
            physics_grades.append(float(item[1]))
            language_grades.append(float(item[2]))
    average_math = sum(math_grades) / len(math_grades)
    average_physics = sum(physics_grades) / len(physics_grades)
    average_language = sum(language_grades) / len(language_grades)
    output = f"{round(average_math, 11)} {round(average_physics, 11)} {round(average_language, 11)}"
    return output


with open(input_file, 'r') as dataset_file:
    input_data = dataset_file.read().strip().split("\n")

students_grades_list = separate_students(input_data)
average_per_student = find_average_grade(students_grades_list)
average_per_subject = find_average_per_subject(students_grades_list)


with open(output_file, 'w') as reply_file:
    reply_file.write(average_per_student)
    reply_file.write(average_per_subject)
