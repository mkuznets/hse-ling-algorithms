def sym_diff(a, b):
    """
    Возвращает симметрическую разность двух массивов.
    Исходные массивы считать отсортированными
    и не содержащими повторяющихся элементов.
    >>> sym_diff([1, 2, 3, 4, 5], [2, 4, 10])
    [1, 3, 5, 10]
    """

    result = []
    for r in a:
        if r not in b:
            result.append(r)
    for r2 in b:
        if r2 not in a and r2 not in result:
            result.append(r2)

    return result
print(sym_diff([1, 2, 3, 4, 5], [2, 4, 10]))
