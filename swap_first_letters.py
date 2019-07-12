import sys
import re




def find_occurrences():
	lines = ['this is a text', "\"this' !is. n1ce,"]
	for line in lines:
		line = line.rstrip()
		splitted_line = line.split(' ')
		new_line = []
		for word in splitted_line:
			if len(word) >= 2:
				first_replacement = re.sub(word[0], word[1], re.escape(word), re.IGNORECASE)
				new_line.append(re.sub(first_replacement[1], word[0], re.escape(first_replacement), 1, re.IGNORECASE))
		print(new_line)


find_occurrences()