def sym_diff(a, b):
    """
    Возвращает симметрическую разность двух массивов.
    Исходные массивы считать отсортированными
    и не содержащими повторяющихся элементов.
    >>> sym_diff([1, 2, 3, 4, 5], [2, 4, 10])
    [1, 3, 5, 10]
    """
    result = []
    ind_a = 0
    ind_b = 0
    while len(a) > ind_a and len(b) > ind_b:
        if a[ind_a] < b[ind_b]:
            result.append(a[ind_a])
            ind_a += 1
        elif b[ind_b] < a[ind_a]:
            result.append(b[ind_b])
            ind_b += 1
        else:
            ind_a += 1
            ind_b += 1
    while len(a) > ind_a:
        result.append(a[ind_a])
        ind_a += 1
    while len(b) > ind_b:
        result.append(b[ind_b])
        ind_b += 1
    return result

# print(sym_diff([1, 2, 3, 4, 5, 11, 48], [2, 4, 10, 11, 12]))
# print(sym_diff([1], [1]))
# print(sym_diff([1, 2, 3, 4, 5], [2, 4, 10]))

