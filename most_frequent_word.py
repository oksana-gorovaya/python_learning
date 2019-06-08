"""Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.
abc a bCd bC AbC BC BCD bcd ABC

"""
with open('/home/xenia/Завантаження/dataset_3363_3 (1).txt', 'r') as dataset_file:
    text = dataset_file.read().strip().lower().split(' ')


def create_set(text):
    words_set = set()
    for item in text:
        words_set.add(item)
    return words_set


def count_words(text, words_set):
    output = {}
    for item in words_set:
        output.update({item: text.count(item)})
    return output


def find_most_frequent_word(biggest_number_of_occurrences, words_statistic):
    most_frequent_words_list = []
    for key, value in words_statistic.items():
        if value == biggest_number_of_occurrences:
            most_frequent_words_list.append(key)
    if len(most_frequent_words_list) > 1:
        most_frequent_words_list.sort()
    return most_frequent_words_list[0]


def build_output(frequent_word, biggest_number_of_occurrences):
    return frequent_word + " " + str(biggest_number_of_occurrences)


words_set = create_set(text)
words_statistic = count_words(text, words_set)
biggest_number_of_occurrences = max(words_statistic.values())
frequent_word = find_most_frequent_word(biggest_number_of_occurrences, words_statistic)
output = build_output(frequent_word, biggest_number_of_occurrences)


with open('/home/xenia/Документи/reply.py', 'w') as result_file:
    result_file.write(output)