def sym_diff(a, b):
    """
    Возвращает симметрическую разность двух массивов.
    Исходные массивы считать отсортированными
    и не содержащими повторяющихся элементов.
    >>> sym_diff([1, 2, 3, 4, 5], [2, 4, 10])
    [1, 3, 5, 10]
    """
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            result.append(a[0])
            a = a[1:]
        elif b[0] < a[0]:
            result.append(b[0])
            b = b[1:]
        else:
            a = a[1:]
            b = b[1:]
    if len(a) > 0:
        result.extend(a)
    if len(b) > 0:
        result.extend(b)
    return result

# print(sym_diff([1, 2, 3, 4, 5, 11, 48], [2, 4, 10, 11, 12]))
# print(sym_diff([1], [1]))

