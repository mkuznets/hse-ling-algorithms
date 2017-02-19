def QuickSort(A):
    if A:
        return QuickSort([x for x in A if x<A[0]]) + [x for x in A if x==A[0]] + QuickSort([x for x in A if x>A[0]])
    return []
    
def nsmallest(m, A):
    q = QuickSort(A)
    print (q[:m:])

    
    """
    Возвращает `m` наименьших элементов массива A.
    Функция реализована на основе Quicksort.
    >>> nsmallest(3, [44, 64, 21, 86, 40, 46, 95])
    [21, 40, 44]
    """
print(nsmallest(4,[44, 64, 21, 86, 40, 46, 95]))

