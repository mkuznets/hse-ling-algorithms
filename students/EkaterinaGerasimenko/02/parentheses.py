def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    parstack = []
    pars = {')':'(',
            ']':'[',
            '}':'{'}
    for i in s:
        if i not in pars:
            parstack.append(i)
        else:
            if parstack and parstack[-1] == pars[i]:
                parstack.pop()
            else:
                return False
    return not parstack