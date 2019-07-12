import sys
import re

pattern = r"(\w+)\1"
substitution_string = 'argh'


def find_occurrences(pattern, substitution_string):
	for line in sys.stdin:
		line = line.rstrip()
		if re.match(pattern, line):
			print(line)
		#print(re.sub(pattern, substitution_string, line, 1, re.IGNORECASE))


find_occurrences(pattern, substitution_string)