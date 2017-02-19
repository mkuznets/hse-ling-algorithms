class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in dict.values():
                stack.append(i)
            else:
                if stack != [] and stack[-1] == dict[i]:
                    stack.pop()
                else:
                    return False
        return stack == []
    