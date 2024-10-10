def getPairsCount(arr, n, k):
    # code here
    # count = 0
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if arr[i] + arr[j] == k:
    #                 count+=1    
    # return count  
 
    c=0
    mp={}
    for i in range(n):
        target=k-arr[i]
        if target in mp:
            c+=mp[target]
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    return c        

k = 6
arr= [ 1, 5, 7, 1]
# arr= [ 1, 1, 1, 1]

n = len(arr)
print(getPairsCount(arr, n, k))