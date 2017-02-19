class Solution:
    def sym_diff(self, a, b):
        result = []
        both = a + b
        for i in range(0, len(both)):
            if ((both[i] not in a) or (both[i] not in b)) and (both[i] not in result):
                 result[len(result):] = [both[i]]
        return result
