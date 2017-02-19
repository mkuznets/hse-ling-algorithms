def partition(A, lo, hi):
    i = 0
    while i <= hi:
        if A[i] == 'W':  # оставить на месте
            i += 1
        elif A[i] == 'R':  # подвинуть в начало
            A[lo], A[i] = A[i], A[lo]
            lo += 1
            i += 1
        else:  # подвинуть в конец
            A[hi], A[i] = A[i], A[hi]
            # i += 1
            hi -= 1
    return A

def three_sort(A):
    """
    Делает in-place сортировку массива с элементами 'B', 'R', 'W'
    по цветам флага Нидерландов. Время работы: O(n).
    >>> three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W'])
    >>> ['R', 'R', 'R', 'W', 'W', 'W', 'B', 'B', 'B']
    """
    return partition(A, 0, len(A)-1)

# print(three_sort(['B', 'B', 'R', 'R', 'W', 'W', 'W', 'R', 'B']))
# print(three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W']))
# print(three_sort(['W', 'W', 'W', 'R', 'B', 'B', 'B', 'R', 'R', 'R']))
