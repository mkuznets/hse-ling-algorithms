def partition(A, pivot, rightcolor):
    # Возможно, в этой процедуре потребуются
    # небольшие изменения
	
	i = 0
	left = 0
	right = len(A)-1
	
	while i <= right:
		if A[i] == pivot:
			i += 1
		elif A[i] == rightcolor:
			A[right], A[i] = A[i], A[right]
			right -= 1
			i += 1
		else:
			A[left], A[i] = A[i], A[left]
			left += 1
			i += 1
	return A


def three_sort(A):
    """
    Делает in-place сортировку массива с элементами 'B', 'R', 'W'
    по цветам флага Нидерландов. Время работы: O(n).
    >>> three_sort(['B', 'B', 'W', 'R', 'B', 'R', 'R', 'W', 'W'])
    >>> ['R', 'R', 'R', 'W', 'W', 'W', 'B', 'B', 'B']
    """
    return partition(A, 'W', 'B')