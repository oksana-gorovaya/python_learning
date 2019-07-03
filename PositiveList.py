"""Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное
целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое
число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.

"""


class NonPositiveError(Exception):
    pass


class NonIntegerError(Exception):
    pass


class PositiveList(list):
    def append(self, c):
        if isinstance(c, int):
            if c <= 0:
                raise NonPositiveError

            super(PositiveList, self).append(c)
        else:
            raise NonIntegerError


new_list = PositiveList()
print(new_list)
new_list.append(-7.0)
print(new_list)