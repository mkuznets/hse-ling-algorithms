def get_idx(A):
    line = 0
    ind = 0
    while ind != len(A)-1:
        if A[line][ind] == 0:
            ind += 1
        elif A[line][ind] == 1:
            line = ind
            ind +=1

    return line



