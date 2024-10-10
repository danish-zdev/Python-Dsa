def rowWithMax1s(arr, n, m):
    # code here
    
    row = -1
    i = 0
    j = m-1
    
    while i < n and j>=0:
        if arr[i][j] == 1:
            row=i
            j-=1
        if arr[i][j] == 0:
            i+=1
    return row 

arr = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
n = len(arr)
m = len(arr)
print(rowWithMax1s(arr, n, m))    