import sys
import re

pattern = r"(\bcat\b)+"


def find_occurrences(pattern):
	for line in sys.stdin:
		line = line.rstrip()
		if re.findall(pattern, line):
			print(line)


find_occurrences(pattern)