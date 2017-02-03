array = [3, 8, 0, 7, 5, 0, 0]
i = 0
for a in range(len(array)):
    if array[a] != 0:
        array[i] = array[a]
        i += 1
for a in reversed(range(i, len(array))):
    array[a] = 0
print(array)
