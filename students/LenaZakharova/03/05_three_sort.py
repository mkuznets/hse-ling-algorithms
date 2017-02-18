def partition(A, lo, hi):
    # Возможно, в этой процедуре потребуются
    # небольшие изменения

    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        # if A[j] <= pivot:
        if (A[j] == 'R' and pivot == 'W') or (A[j] == 'W' and
                pivot == 'B') or (A[j] == pivot) or (A[j] == 'R' and pivot == 'B'):
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    return i


def pre_sort(li, first, last):
    if first < last:
        pivot = partition(li, first, last)
        pre_sort(li, first, pivot - 1)
        pre_sort(li, pivot + 1, last)
    return li


def three_sort(A):
    """
    Делает in-place сортировку массива с элементами 'B', 'R', 'W'
    по цветам флага Нидерландов. Время работы: O(n).
    >>> three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W'])
    >>> ['R', 'R', 'R', 'W', 'W', 'W', 'B', 'B', 'B']
    """
    return pre_sort(A, 0, len(A)-1)

# print(three_sort(['B', 'B', 'R', 'R', 'W', 'W', 'W', 'R', 'B']))
# print(three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W']))
# print(three_sort(['W', 'W', 'W', 'R', 'B', 'B', 'B', 'R', 'R']))
