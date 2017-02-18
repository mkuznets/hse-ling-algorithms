def partition(A, lo, hi):
    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    return i

def QuickSort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        QuickSort(A,lo,p-1)
        QuickSort(A,p+1,hi)

def nsmallest(m, A):
    QuickSort(A, 0, len(A)-1)
    return A[:m:]

    
    """
    Возвращает `m` наименьших элементов массива A.
    Функция реализована на основе Quicksort.
    >>> nsmallest(3, [44, 64, 21, 86, 40, 46, 95])
    [21, 40, 44]
    """
print(nsmallest(4,[44, 64, 21, 86, 40, 46, 95]))

