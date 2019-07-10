"""Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза."""
import sys
import re

pattern = r"(.*cat.*){2,}"


def find_occurrences(pattern):
	for line in sys.stdin:
		line = line.rstrip()
		if re.findall(pattern, line):
			print(line)


find_occurrences(pattern)