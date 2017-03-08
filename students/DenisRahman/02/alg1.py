
def movezeroes(list):
    for i in range (len(list)):
        if list[i] == 0:
            del list[i]
            list.append(0)
    return list

print (movezeroes([0,1,2,0,3,4,5,0]))