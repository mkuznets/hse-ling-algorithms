def sym_diff(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        elif a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        elif a[0] == b[0]:
            a.remove(a[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c
