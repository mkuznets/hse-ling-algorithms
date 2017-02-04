class Solution(object):
    def isValid(self, s):
        stack = []
        d = {")":"(","}":"{","]":"["}
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack == [] or d[i] != stack.pop():
                    return False
            else:
                return False
        return True
