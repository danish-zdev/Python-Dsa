def trappingWater(arr,n):
    #Code here
    left = [0]*n
    left[0] = arr[0]

    right = [0]*n
    right[n-1] = arr[n-1]

    ans = 0

    for i in range(1,n):
        left[i] = max(arr[i],left[i-1])

    for i in range(n-2,-1,-1):
        right[i] = max(arr[i],right[i+1])

    for i in range(1,n-1):
        ans = ans + min(left[i],right[i]) - arr[i]

    return ans


arr = [3,0,0,2,0,4]   
n = len(arr)

print(trappingWater(arr,n))