"""Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
вывести получившуюся статистику.
a aa abC aa ac abc bcd a
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз."""

user_input = input().lower().split(' ')


def create_set(user_input):
    words_set = set()
    for item in user_input:
        words_set.add(item)
    return words_set


def count_words(user_input, words_set):
    output = ''
    for item in words_set:
        output += item + ' ' + str(user_input.count(item)) + "\n"
    return output


words_set = create_set(user_input)
print(count_words(user_input, words_set))
