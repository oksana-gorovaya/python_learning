import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import re
#http://pastebin.com/raw/2mie4QYa
#http://pastebin.com/raw/hfMThaGb
#'http://pastebin.com/raw/hfMThaGb
url = input().strip()
file_location = '/home/xenia/Завантаження/new'
urllib.request.urlretrieve(url, file_location)
with open(file_location) as html_file:
	file = html_file.readlines()


def extract(content):
	links = []
	soup = BeautifulSoup(content, 'lxml')
	for tag in soup.find_all('a', href=True):
		links.append(tag['href'])
	return links


def get_links_list(file):
	links_list = []
	pattern1 = r'(href)=\s+'
	pattern2 = r'(href)\s+='
	for item in file:
		if item != '\n' and (re.findall(pattern1, item) == []) and (re.findall(pattern2, item) == []):
			if extract(item):
				links_list.append(extract(item))
	return links_list


def find_domains(links_list):
	domains_list = set()
	for item in links_list:
		domain = urllib.parse.urlparse(item[0]).netloc
		if domain:
			if domain.rfind(':') != -1:
				domains_list.add(domain[:domain.rfind(":")])
			else:
				domains_list.add(domain)
		else:
			if item[0].startswith('..') == False:
				domains_list.add(urllib.parse.urlparse(item[0]).path)

	return sorted(list(domains_list))


links_list = get_links_list(file)
sorted_links = find_domains(links_list)
reply = ''
for item in sorted_links:
	reply += item + '\n'

print(reply)



