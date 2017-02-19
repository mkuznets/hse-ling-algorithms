def partition(A,pivotletter,leftletter):
    # Возможно, в этой процедуре потребуются
    # небольшие изменения
    j = 0
    left = 0
    right = len(A) - 1
    
    while j <= right:
        if A[j] == leftletter:
            A[left], A[j] = A[j], A[left]
            left += 1
            j += 1
        elif A[j] == pivotletter:
            j += 1
        else:
            A[right], A[j] = A[j], A[right]
            right -= 1


def three_sort(A):        
    """
    Делает in-place сортировку массива с элементами 'B', 'R', 'W'
    по цветам флага Нидерландов. Время работы: O(n).
    >>> three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W'])
    >>> ['R', 'R', 'R', 'W', 'W', 'W', 'B', 'B', 'B']
    """
    partition(A,'W','R')
