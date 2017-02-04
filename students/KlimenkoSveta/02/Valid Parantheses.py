class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(':')','{':'}', '[':']'}
        list = []
        print(len(s))
        for i in s:
            if i in pairs:
                list.append(i)
            else:
                if list != [] and i == pairs[list[-1]]:
                    list.pop(-1)
                else:
                    return False
        return list == []