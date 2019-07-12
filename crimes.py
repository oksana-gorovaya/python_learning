import csv

with open('/home/xenia/Завантаження/Crimes.csv', 'r') as dataset_file:
	reader = csv.DictReader(dataset_file)
	crimes = []
	for row in reader:
		for key, value in dict(row).items():
			if key == 'Primary Type':
				crimes.append(value)


def find_crime_frequency(crimes):
	crime_statistic = set()
	for crime in crimes:
		crime_statistic.add(tuple((crime, crimes.count(crime))))

	return dict(crime_statistic)


def find_most_frequent_crime(crime_statistic):
	max_number = max(crime_statistic.values())
	result = []
	for key, value in crime_statistic.items():
		if value == max_number:
			result.append(key)

	return sorted(result)[0]

crime_statistic = find_crime_frequency(crimes)
print(find_most_frequent_crime(crime_statistic))