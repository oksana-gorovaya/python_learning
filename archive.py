from zipfile import ZipFile
import os
import tempfile

file_name = input('Enter path to source zip file: ')


with tempfile.TemporaryDirectory() as extraction_directory:
	with ZipFile(file_name, 'r') as zipfile:
		zipfile.extractall(extraction_directory)
		sample_dir = os.listdir(extraction_directory)
		high_lvl_items = os.walk(extraction_directory + '/' + ''.join(sample_dir))
		py_directories = set()
		for address, dirs, files in high_lvl_items:
			for file in files:
				if file.endswith('.py'):
					py_directories.add(''.join(address.split(extraction_directory + '/')))
		sorted_dirs = sorted(py_directories)

	with open(input('Enter path to output file: '), 'w') as reply_file:
		for path in sorted_dirs:
			reply_file.write(path + '\n')

