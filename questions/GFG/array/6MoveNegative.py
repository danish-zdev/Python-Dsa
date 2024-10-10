
arr = [1, -1, 3, 2, -7, -5, 11, 6] 
temp = 0
for i in range(len(arr)):
    if arr[i]<0:
        arr[i], arr[temp] = arr[temp], arr[i]
        temp+=1    

print(arr)   