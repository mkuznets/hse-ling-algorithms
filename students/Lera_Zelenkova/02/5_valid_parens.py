class Solution(object):
    def isValid(self, s):
        alles = []
        dict_ = {')':'(', ']':'[', '}':'{'}
        for elem in s:
            if elem in dict_.values():
                alles.append(elem) # это начало стека - аппендим открывающую скобочку
            elif elem in dict_.keys():
                if not alles:
                    return False
                if dict_[elem] != alles[-1]:
                    return False
                else:
                    alles = alles[:-1:]
        if not alles:
            return True
        else:
            return False