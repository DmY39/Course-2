# Реализуйте структуру данных, представляющую собой расширенную структуру стек.
# Выполнение какой-либо операции с последними 2-ми элементами списка и добавление результата в конец списка


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())



