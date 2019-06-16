import requests
import re


def check_files():
    file_name = '699991.txt'
    while re.match(r'(^[0-9]+[.]txt$)', file_name):
        path = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + file_name)
        file_name = path.text
    return file_name


print(check_files())
