"""Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
повторов, и производит обратную операцию, получая исходный текст.
L4V7H18O20a9m20R18Q2h12x9P12l15o19B3H17f15q17o10N11U11S13f10q6Q17W14U4p16w3S6M2A1a11r1J12

"""
import re


with open(input('Path to dataset file:'), 'r') as encoded_file:
    encoded_string = encoded_file.readline().strip()


pattern = '[a-zA-Z]+'


def split_input(encoded_string, pattern):
    data_array = []
    for item in encoded_string:
        if re.search(pattern, item):
            chunk = re.sub(pattern, f",{item}", item)
            data_array.append(chunk)
        else:
            data_array.append(item)

    string_chunks = "".join(data_array)
    return string_chunks.split(",")


def restore_letter_blocks(splited_input, pattern):
    result = []
    for item in splited_input:
        if item != "":
            letters = []
            numbers = []
            for element in item:
                if re.search(pattern, element):
                    letters.append(element)
                else:
                    numbers.append(element)
            duplicate_amount = "".join(numbers)
            letter_block = letters[0] * int(duplicate_amount)
            result.append(letter_block)
    return result


def decode_final_string(restored_blocks):
    return "".join(restored_blocks)


splited_input = split_input(encoded_string, pattern)
restored_blocks = restore_letter_blocks(splited_input, pattern)
initial_string = decode_final_string(restored_blocks)

with open(input('Path to output file:'), 'w') as decoded_file:
    decoded_file.write(initial_string)