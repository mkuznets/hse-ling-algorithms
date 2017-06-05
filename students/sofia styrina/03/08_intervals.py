class Solution:
    def intervals(self, A, B):
        segments = []
        for i in range(len(A)):
            segments.append((A[i], -1))
            segments.append((B[i], 1))
        segments.sort()
        result = 0
        x = 0
        for a, b in segments:
            if b == -1: result += x
            x -= b
        return result
