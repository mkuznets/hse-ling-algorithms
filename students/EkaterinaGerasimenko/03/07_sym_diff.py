def sym_diff(a, b):
    """
    Возвращает симметрическую разность двух массивов.
    Исходные массивы считать отсортированными
    и не содержащими повторяющихся элементов.
    >>> sym_diff([1, 2, 3, 4, 5], [2, 4, 10])
    [1, 3, 5, 10]
    """
    result = []
    first,second = 0,0
    while first < len(a) and second < len(b):
        if a[first] < b[second]:
            result.append(a[first])
            first += 1
        elif a[first] > b[second]:
            result.append(b[second])
            second += 1
        else:
            first += 1
            second += 1
    while first < len(a):
        result.append(a[first])
        first += 1
    while second < len(b):
        result.append(b[second])
        second += 1        
    return result      

