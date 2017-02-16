def get_idx(A):
    for i in range(len(A)):
        if (sum(A[i]) - A[i][i] == 0):
            s = 0
            for j in range(len(A)):
                if j != i:
                    s += A[j][i]
            if s == len(A) - 1:
                break
    return i

print(get_idx([[0, 1, 0], [0, 1, 0], [1, 1, 1]]))
