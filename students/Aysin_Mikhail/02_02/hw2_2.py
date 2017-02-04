# coding: utf-8

def find_index_naive(L, what):
    for i in range(len(L)):
        if L[i] == what:
            return i
    return -1

def find_index_bisection(L, what):
    i_left = 0
    i_right = len(L)-1
    i_mid = (i_left + i_right)//2
    while i_left < i_right:
        if L[i_mid] == what:
            return i_mid
        elif L[i_mid] < what:
            i_left = i_mid + 1
        else:
            i_right = i_mid - 1
        i_mid = (i_left + i_right)//2
    return -1


# L = [i for i in range(1, 22, 2)]
# L = [0, 1, 1, 2, 3, 5, 8, 13, 201]
#print('*')
#print(find_index_naive(L, 10))
#print('*')
#print(find_index_bisection(L, 10))

def find_index_min(L):
    i_left = 0
    i_right = len(L)-1
    i_mid = (i_left + i_right)//2
    while True:
        if i_left == i_mid:
            return L[i_right]
        elif i_left == i_right:
            return L[i_left]

        if L[i_left] > L[i_mid] and L[i_right] > L[i_mid]:
            i_right = i_mid
        else:
            i_left = i_mid + 1
        i_mid = (i_left + i_right) // 2



#     0   1   2   3   4   5   6
#              LM  R
L  = [12, 13, 14, 8,  9,  10, 11]   # M<L, M<R  ->  min на середине
print(find_index_min(L))
#     LM  R
L2 = [14, 8,  9,  10, 11, 12, 13]   # M<L, M<R  ->  min слева
print(find_index_min(L2))
#                             LR
L3 = [9,  10, 11, 12, 13, 14, 8]    # M>L, M>R  ->  min справа
print(find_index_min(L3))
#если L совпадает с M, то минимум на R
#если L совпадает с R, то минимум на LR

#L = [4,5,6,7,0,1,2]