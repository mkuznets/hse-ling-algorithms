def key(x):
    # Функция вычисления ключа сравнения для `sorted`.
    # Перепишите её так, чтобы она реализовала
    # натуральную сортировку строк состоящих из символов a-z0-9.

    # Функция не должна использовать регулярные выражения!

    # Для "обычной" посимвольной сортировки она могла
    # бы выглядеть так:
    # return tuple(c for c in x)
    res = []
    ind = 0
    str_num = ''

    while ind < len(x):
        if x[ind] in '0123456789':
            str_num += x[ind]
            ind += 1
        else:
            res.append(x[ind])
            ind += 1
    res.append(int(str_num))
    return res

# print(sorted(['lol3', 'a10', 'lol2', 'lol20', 'lol100', 'lol11', 'lol21', 'a1'], key=key))
