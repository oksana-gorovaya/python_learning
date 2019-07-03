import datetime


def convert_input(date):
	return list(map(lambda item: int(item), date.split(' ')))


def calculate_date(start_date, days):
	end_date = start_date + datetime.timedelta(days=days)

	return str(end_date.year) + ' ' + str(end_date.month) + ' ' + str(end_date.day)


date = input()
days = int(input())
converted_input = convert_input(date)
start_date = datetime.date(*converted_input)
print(calculate_date(start_date, days))