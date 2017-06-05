def partition(A, lo, hi):

    # Возможно, в этой процедуре потребуются
    # небольшие изменения

    # pivot = A[hi]
    # i = lo
    #
    # for j in range(lo, hi):
    #     if A[j] <= pivot:
    #         A[i], A[j] = A[j], A[i]
    #         i += 1
    #
    # A[i], A[hi] = A[hi], A[i]
    # return i

    l = 0
    h = len(A) - 1
    j = 0

    while j <= h:
        if A[j] == hi:
            A[l], A[j] = A[j], A[l]
            l += 1
            j += 1
        elif A[j] == lo:
            j += 1
        else:
            A[h], A[j] = A[j], A[h]
            h -= 1


def three_sort(A):
    """
    Делает in-place сортировку массива с элементами 'B', 'R', 'W'
    по цветам флага Нидерландов. Время работы: O(n).

    three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W'])
    ['R', 'R', 'R', 'W', 'W', 'W', 'B', 'B', 'B']

    """
    partition(A, 'W', 'R')

    return A

    pass

#print(three_sort(['W', 'W', 'B', 'R', 'B', 'R', 'B', 'W', 'R']))