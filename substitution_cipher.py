"""В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили
каким-то странным набором звуков.
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е.
заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь
 нуждаются в помощи:
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
"""

initial_letters = input()
encrypting_letters = input()
string_to_encrypt = input()
string_to_decrypt = input()


def to_dictionary(initial_letters, encrypting_letters):

    return dict(zip(list(initial_letters), list(encrypting_letters)))


def encrypt_string(cipher_key, string_to_encrypt):
    encrypted_string = ''
    for item in string_to_encrypt:
        if item in cipher_key.keys():
            encrypted_string += cipher_key[item]

    return encrypted_string


def decrypt_string(cipher_key, string_to_decrypt):
    decrypted_string = ''
    for item in string_to_decrypt:
        if item in cipher_key.values():
            for key, value in cipher_key.items():
                if item == value:
                    decrypted_string += key

    return decrypted_string


cipher_key = to_dictionary(initial_letters, encrypting_letters)
encrypted_string = encrypt_string(cipher_key, string_to_encrypt)
decrypted_string = decrypt_string(cipher_key, string_to_decrypt)
print(encrypted_string)
print(decrypted_string)