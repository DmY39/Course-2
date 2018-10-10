#  Программа, которая эмулирует пространство имен.
# Есть запросы создания пространства, добавление переменных в пространство
# и получение имени пространство

n = int(input())
a = []
dict = {'global': [None, set()]}
for i in range(n):
    act, name, var = input().split()

    if act == 'create': # Если запрос на создание множества, то создадим список
        dict[name] = [var, set()]

    if act == 'add': # если запрос на добавление переменной
        dict[name][1].add(var)

    if act == 'get': # Запрос на вывод неймспейса
            while var not in dict[name][1]:
                name = dict[name][0]
                if name == None:
                    break
            a.append(name)
for i in a:
    print(i)
