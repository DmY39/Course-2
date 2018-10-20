d = {}
n = int(input())
for i in range(n):
    a = list(input().split())
    if len(a) == 1:
        d[a[0]] = []
    else:
        d[a[0]] = a[2:]
        for i in a[2:]:  # Для создания в словаре ключей, которые не были добавлены
            if i not in d:
                d[i] = []

# print(d)
def path(predok, class2):
    if predok and class2 not in d.keys():
        return 'No'
    elif predok == class2:
        return 'Yes'
    elif predok in d[class2]:
        return 'Yes'
    for elem in d[class2]:   # для каждого элемента по ключу class2
        if predok not in d[class2]: # если предка нет в списке по ключу class 2
            class2 = elem # то присваем классу2 значение элемента по ключу этого класса
            # print(d[elem], 'is elem')
            # print(class2, 'is class 2')
            path(predok, class2) # выполняем функцию в рекурсии
            if path(predok, class2) == 'Yes': # если функция возвращает Да, то сворачиваем рекурсию
                return 'Yes'
    return 'No'
q = int(input())
for i in range(q):
    predok, class2 = list(input().split())
    # print(predok, class2)
    print(path(predok, class2))
