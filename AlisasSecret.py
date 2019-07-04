"""Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из
паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей
служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы."""
from simplecrypt import decrypt

with open(input(), "rb") as input_file:
	encrypted = input_file.read()


with open(input(), "r") as passwords_file:
	passwords = passwords_file.readlines()


def decrypt_file(passwords, encrypted):

	for password in passwords:
		try:
			print(decrypt(password.strip(), encrypted).decode('utf8'))
		except:
			continue


decrypt_file(passwords, encrypted)