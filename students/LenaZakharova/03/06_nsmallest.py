def partition(A, lo, hi):
    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    return i


def pre_sort(li, first, last, m):
    if last - first >= m:
        pivot = partition(li, first, last)
        pre_sort(li, first, pivot - 1, m)
        pre_sort(li, pivot + 1, last, m)
    return li


def nsmallest(m, A):
    """
    Возвращает `m` наименьших элементов массива A.
    Функция реализована на основе Quicksort.
    >>> nsmallest(3, [44, 64, 21, 86, 40, 46, 95])
    [21, 40, 44]
    """
    return pre_sort(A, 0, len(A)-1, m)[:m]

# print(nsmallest(4, [44, 64, 21, 86, 40, 46, 95]))
# print(nsmallest(2, [1, 64, 86, 40, 46, 95]))
# print(nsmallest(2, [1, 1, 1, 1, 46, 95]))
# print(nsmallest(6, [44, 64, 21, 86, 40, 46, 95]))