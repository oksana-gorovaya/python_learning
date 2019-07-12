import sys
import re

pattern = r"\b[a-z]*?([a-z]{2,}?)\1+[a-z]*?\b" # r"\b(\w+)\?{2}\b"


def find_occurrences(pattern):
	for line in sys.stdin:
		line = line.rstrip()
		print(line)
		if re.findall(pattern, line):
			print(line)


find_occurrences(pattern)