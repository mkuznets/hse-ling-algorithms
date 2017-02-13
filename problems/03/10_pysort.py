def key(x):
    # Функция вычисления ключа сравнения для `sorted`
    # реализующая натуральную сортировку строк
    # аналогичную команде `sort -V`.
    # Предполагается, что строки будут состоять из 

    # Для "обычной" посимвольной сортировки она могла
    # бы выглядеть так:
    return tuple(c for c in x)


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
