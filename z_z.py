import sys
import re

pattern = r"z(.){3}z"


def find_occurrences(pattern):
	for line in sys.stdin:
		line = line.rstrip()
		if re.findall(pattern, line):
			print(line)


find_occurrences(pattern)