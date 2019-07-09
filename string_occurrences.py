"""Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s."""
s = input()
t = input()


def find_occurrences(s, t):
	count = start = 0
	while True:
		start = s.find(t, start) + 1
		if start > 0:
			count += 1
		else:
			return count


print(find_occurrences(s, t))