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
    >>> nsmallest(3, [44, 64, 21, 86, 40, 46, 95])
    [21, 40, 44]
    """
    smallest = quicksort_cut(m,A,0,len(A)-1)
    return smallest

def quicksort_cut(m, A, start, end):
    if start >= end:
        return A[:start]
    if start < end:
        pivot = partition(A, start, end)
        if pivot == m:
            return A[:m]
        elif m > pivot:
            return quicksort_cut(m, A, pivot+1, end)
        else:
            return quicksort_cut(m, A, start, pivot-1)