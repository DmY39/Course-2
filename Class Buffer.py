# класс Buffer,
# который будет накапливать в себе элементы последовательности
#  и выводить сумму пятерок последовательных элементов
#  по мере их накопления.


class Buffer:

    def __init__(self):  # constructor without args
        self.posled = []

    def add(self, *a):   # add a part of sequence
        self.posled += a

        # print sum of five elements and del five elem,
        #  while a quantity of list less then 5
        while len(self.posled) >= 5:
            print(sum(self.posled[0:5]))
            del self.posled[0:5]

    def get_current_part(self):
        return self.posled


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]