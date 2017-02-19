def partition(A, lo, hi):
    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    return i


def nsmallest(m, A):
    """
    Возвращает `m` наименьших элементов массива A.
    Функция реализована на основе Quicksort.

    nsmallest(3, [44, 64, 21, 86, 40, 46, 95])
    [21, 40, 44]
    """
    for i in range(0, len(A) - 1):
        p = partition(A, 0, len(A) - 1)
        if i < p:
            partition(A, 0, p - 1)
        else:
            partition(A, p + 1, len(A) - 1)

    return A[:m:]

#print(nsmallest(4, [1, 0, 3, 2, 7, 8, 4, 5]))
