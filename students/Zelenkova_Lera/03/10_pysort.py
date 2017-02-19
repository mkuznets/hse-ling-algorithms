"""
классы:
0 - точка
1 - цифры
3 - буквы
2 - большие буквы
4 - пунктуация
"""

def key(x):
    full_stop = '.'
    alpha_small = 'abcdefghijklmnopqrstuvwxyz'
    alpha_big = alpha_small.upper()
    num = '0123456789'
    punct = '!"#$%&()*+,-/:;<=>?@[\]^_{|}~'
    letters_small = list(alpha_small)
    letters_big = list(alpha_big)
    punct = list(punct)

    indices_small = list(range(0, len(alpha_small)))
    indices_big = list(range(0, len(alpha_big)))
    indices_punct = list(range(0, len(punct)))

    d_small = dict(zip(letters_small, indices_small))
    d_big = dict(zip(letters_big, indices_big))
    d_punct = dict(zip(punct, indices_punct))


    repres = []  # тут репрезентация строки в виде кортежа вида ( int <класс объекта> , int <ранг объекта в классе> )
    found_num = ''  # чтоб запоминать число
    for let in x:
        if let == full_stop:
            if found_num != '':
                repres.append((1, int(found_num)))
                found_num = ''  # если число в начале или в середине, то мы идем пока не встретим букву и тогда аппендим число и удаляем его из found_num
            repres.append((0, 0))
        if let in alpha_small:
            if found_num != '':
                repres.append((1, int(found_num)))
                found_num = ''  # если число в начале или в середине, то мы идем пока не встретим букву и тогда аппендим число и удаляем его из found_num
            repres.append((3, d_small[let]))
        elif let in alpha_big:
            if found_num != '':
                repres.append((1, int(found_num)))
                found_num = ''  # если число в начале или в середине, то мы идем пока не встретим букву и тогда аппендим число и удаляем его из found_num
            repres.append((2, d_big[let]))
        elif let in punct:
            if found_num != '':
                repres.append((1, int(found_num)))
                found_num = ''  # если число в начале или в середине, то мы идем пока не встретим букву и тогда аппендим число и удаляем его из found_num
            repres.append((4, d_punct[let]))
        elif let in num:
            found_num += let
    if found_num != '':  # если число в конце (потому что аппенд был только если мы встретили букву дальше)
        repres.append((1, int(found_num)))
    return repres

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
