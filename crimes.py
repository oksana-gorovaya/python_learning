import csv

with open('/home/xenia/Завантаження/Crimes.csv', 'r') as dataset_file:
	reader = csv.DictReader(dataset_file)
	for row in reader:
		print(row)