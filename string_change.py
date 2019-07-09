"""Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если
операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
или Impossible, если операций потребуется более 1000."""
main_string = input()
first_string = input()
second_string = input()
counter = 0


def count_changes(main_string, first_string, second_string, counter):
	try:
		if first_string in main_string:
			counter += 1
			return count_changes(main_string.replace(first_string, second_string), first_string, second_string, counter)
		else:
			return counter
	except RecursionError:
		return 'Impossible'


print(count_changes(main_string, first_string, second_string, counter))