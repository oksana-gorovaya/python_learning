import sys
import re

pattern = r"\b(a+)\b"
substitution_string = 'argh'


def find_occurrences(pattern, substitution_string):
	for line in sys.stdin:
		line = line.rstrip()
		print(re.sub(pattern, substitution_string, line, 1, re.IGNORECASE))


find_occurrences(pattern, substitution_string)