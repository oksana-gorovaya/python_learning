import sys
import re

pattern = r"human"
substitution_string = 'computer'


def find_occurrences(pattern):
	for line in sys.stdin:
		line = line.rstrip()
		print(re.sub(pattern, substitution_string, line))


find_occurrences(pattern)