def sym_diff(a, b):
    result = []
    for i in range(len(a)):
        if a[i] not in b:
            result.append(a[i])         
    for i in range(len(b)):
        if b[i] not in a:
            result.append(b[i])      
    return result

print(sym_diff([1, 2, 3, 4, 5], [2, 4, 10]))
