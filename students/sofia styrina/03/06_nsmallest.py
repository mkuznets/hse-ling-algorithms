import random
 
class Solution:
    def nsmallest(self, m, A):

        if not 0 <= m <= len(A):
            raise ValueError('not enough elements')
        result = []
        while True:
            pivot = random.choice(A)
            pcount = 0
            under = []
            over = []
            for elem in A:
                if elem < pivot:
                    under.append(elem)
                elif elem > pivot:
                    over.append(elem)
                else:
                    pcount += 1
            if m < len(under):
                A = under
            elif m <= len(under) + pcount:
                result += under
                result += [pivot] * (m - len(under))
                return result
            else:
                result += under
                result += [pivot] * pcount
                A = over
                m -= len(under) + pcount
 

