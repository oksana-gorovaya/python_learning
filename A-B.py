"""Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

"""
import requests

page_a = input().strip()
page_b = input().strip()


def check_page(page):
	try:
		links = []
		res = requests.get(page)
		if res.status_code == 200:
			for item in res.text.split('"'):
				if item.startswith('http'):
					links.append(item)
		return links

	except:
		return 'No'


def compare_pages(page_b, page_content):
	for item in page_content:
		nested_links = check_page(item)
		if page_b in nested_links:
			return 'Yes'

	return 'No'


page_a_content = check_page(page_a)
print(compare_pages(page_b, page_a_content))

