"""Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из
этой последовательности, затем сумму второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
последовательных элементов по мере их накопления.

Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма."""


class Buffer:
    def __init__(self):
        self.container = []

    def add(self, *numbers_array):
        for number in numbers_array:
            self.container.append(number)
        while len(self.container) >= 5:
            print(create_buffer(self.container))

        return self.container

    def get_current_part(self):
        if len(self.container) < 5:
            return self.container
        else:
            self.container = self.container[slice(5, None)]
            return self.container


def create_buffer(container):
    temp_container = []
    counter = 0
    while counter < 5:
        temp_container.append(container.pop(0))
        counter += 1
    return sum(temp_container)


