class Solution:
    def three_sort(self, A):
        i = 0
        j = 0
        b = 0

        while j < len(A):
            if j < len(A):
                if A[j] == 'R':
                    A[j-b] = A[j]
                        
                    A[i], A[j-b] = A[j-b], A[i]
                    j += 1
                    i += 1

            if j < len(A):            
                if A[j] == 'W':
                    A[j-b] = A[j]
                    j += 1

            if j < len(A):
                if A[j] == 'B':
                    A[j-b] = A[j]
                    j += 1
                    b += 1

        bb = len(A) - b    
        while bb < len(A):
            A[bb] = 'B'
            bb += 1

