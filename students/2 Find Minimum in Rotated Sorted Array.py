#Задача 2 (3 балла) Find Minimum in Rotated Sorted Array
arr = [4,5,6,7,0,1,2]
a = 0
for a in range(len(arr)-1):
    if arr[a] > arr[a+1]:
        print(arr[a+1])
