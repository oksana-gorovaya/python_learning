"""Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот
символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
последовательность на стандартный вывод. Кодирование должно учитывать регистр символов."""

DNA_sample = input()
DNA_coded = ''
temp_str = ''
arr = list(DNA_sample)
counter = 0

for item in arr:
    if counter == 0:
        temp_str += f"{item}"
        counter += 1
        continue

    if arr[counter] != arr[counter - 1]:
        temp_str += f",{item}"

    else:
        temp_str += f"{item}"
    counter += 1

temp_array = temp_str.split(',')
for element in temp_array:
    DNA_coded += f"{element[:1]}{len(element)}"
print(DNA_coded)
