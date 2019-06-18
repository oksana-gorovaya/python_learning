"""Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом
тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов,
после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк
текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается.
Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
"""
import itertools


def fill_dynamic_list(entries_number):
    filled_list = []
    while len(filled_list) < entries_number:
        another_entry = input().lower()
        filled_list.append(another_entry)

    return filled_list


def split_lines(text_lines):
    separated_words = []
    for item in text_lines:
        separated_words.append(item.split(' '))

    return list(itertools.chain(*separated_words))


def compare_lists(allowed_words, splitted_lines):
    unrecognized_words = set(splitted_lines) - set(allowed_words)
    formatted_output = ''
    for item in unrecognized_words:
        formatted_output += item + '\n'

    return formatted_output


number_of_words = int(input())
allowed_words = fill_dynamic_list(number_of_words)
number_of_lines = int(input())
text_lines = fill_dynamic_list(number_of_lines)
splitted_lines = split_lines(text_lines)
unrecognized_words = compare_lists(allowed_words, splitted_lines)
print(unrecognized_words)
