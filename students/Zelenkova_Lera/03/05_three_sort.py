def partition(A, begin, end, where=''):
    pivot = A[end]
    i = begin
    if (pivot == 'R' and where=='L') or (pivot=='W' and where=='R'):
        for j in range(begin, end):
            if less_or_eq(A[j], pivot):
                A[i], A[j] = A[j], A[i]
                i += 1
    else:
        for j in range(begin, end):
            if less_than(A[j], pivot):
                A[i], A[j] = A[j], A[i]
                i += 1

    A[i], A[end] = A[end], A[i]
    return i

def less_than(letter_1, letter_2):
    order = ['R', 'W', 'B']
    return order.index(letter_1) < order.index(letter_2)

def less_or_eq(letter_1, letter_2):
    order = ['R', 'W', 'B']
    return order.index(letter_1) <= order.index(letter_2)

def three_sort(A):
    p = partition(A, begin=0, end = len(A)-1, where='L')
    if p+1 < len(A):
        partition(A, begin=p+1, end=len(A)-1, where='R')
    elif p-1 >= 0:
        partition(A, begin=0, end = p-1, where='L')
    return A


