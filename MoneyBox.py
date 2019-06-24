"""Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее
вместимость."""


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins_in_box = 0

    def can_add(self, number_of_coins):
        if (self.capacity - self.coins_in_box) >= number_of_coins:
            return True
        return False

    def add(self, number_of_coins):
        self.coins_in_box += number_of_coins
        return self.coins_in_box


small_money_box = MoneyBox(7)



