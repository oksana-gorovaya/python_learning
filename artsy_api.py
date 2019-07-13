import requests
import json

client_id = '75b44e45ed6ec0dca6bc'
client_secret = 'e0eafb455681e67ca0357a6c32bfbd49'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
				data={
					"client_id": client_id,
					"client_secret": client_secret
				})

j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token" : token}


def get_artists():
	with open('/home/xenia/Завантаження/dataset_24476_4 (2).txt', 'r') as dataset_file:
		data = dataset_file.readlines()
		artists = []
		for artist_id in data:
			r = requests.get("https://api.artsy.net/api/artists/" + artist_id.strip(), headers=headers)

			j = json.loads(r.text)
			artists.append(tuple((j["sortable_name"], j["birthday"])))

		return artists


def sort_artists(artists):
	return sorted(sorted(artists, key = lambda artist: artist[0]), key = lambda artist: artist[1])


artists = get_artists()
sorted_artists = sort_artists(artists)
for item in sorted_artists:
	print(item[0])