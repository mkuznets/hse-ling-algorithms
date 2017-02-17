def partition(A, lo, hi):
    # Возможно, в этой процедуре потребуются
    # небольшие изменения

    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    return i


def three_sort(A):
    """
    Делает in-place сортировку массива с элементами 'B', 'R', 'W'
    по цветам флага Нидерландов. Время работы: O(n).
    >>> three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W'])
    >>> ['R', 'R', 'R', 'W', 'W', 'W', 'B', 'B', 'B']
    """
    pass
