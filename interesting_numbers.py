import requests
import json

with open('/home/xenia/Завантаження/dataset_24476_3.txt', 'r') as dataset_file:
	data = dataset_file.readlines()
	for number in data:
		received_item = requests.get('http://numbersapi.com/' + str(number.strip()) + '/math?json=true').content
		for key, value in json.loads(received_item).items():
			if key == 'found':
				if value:
					print('Interesting')
				else:
					print('Boring')