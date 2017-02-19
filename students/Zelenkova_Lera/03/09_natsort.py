def key(x):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    letters = list(alpha)
    indices = list(range (-25, -1 ) )
    d = dict(zip(letters, indices)) 

    repres = []  #тут репрезентация строки в виде цифр
    found_num = ''  #чтоб запоминать число
    for i in x:
        if i in alpha:
            if found_num != '':
                repres.append(int(found_num))
                found_num = '' #если число в начале или в середине, то мы идем пока не встретим букву и тогда аппендим число и удаляем его из found_num
            repres.append(d[i])
        elif i in num:
            found_num+=i
    if found_num != '':  #если число в конце (потому что аппенд был только если мы встретили букву дальше)
        repres.append(int(found_num))
    return repres
