def key(x):
    # Функция вычисления ключа сравнения для `sorted`
    # реализующая натуральную сортировку строк
    # аналогичную команде `sort -V`.
    # Предполагается, что строки будут состоять из

    # Для "обычной" посимвольной сортировки она могла
    # бы выглядеть так:
    res = []
    ind = 0
    str_num = ''
    while ind < len(x):
        if x[ind] in '0123456789':
            str_num += x[ind]
            ind += 1
        elif x[ind] in '.~':
            res.append(ord(x[ind])-1000)
            ind += 1
        elif x[ind] in '!"#*$%&\'()+,-/:;<=>?@[\]^_`{|}':
            res.append(ord(x[ind])+120)
            ind += 1
        else:
            str_num = ''
            res.append(ord(x[ind]))
            ind += 1
    if str_num != '':
        res.append(int(str_num))
    return res


if __name__ == '__main__':
    # Читаем строки из файла, переданного в команду
    # первым аргументом, сортируем, печатаем на экран.

    import sys
    try:
        filename = sys.argv[1]
        fp = open(filename, 'r')
    except KeyError:
        fp = sys.stdin

    lines = map(str.strip, fp.readlines())
    fp.close()

    lines = sorted(lines, key=key)
    print("\n".join(lines))

