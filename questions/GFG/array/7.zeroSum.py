def zeroSum(arr,n):
    sum1 = 0
    dic = {}
    for ind in range(n):
        sum1+=arr[ind]
        if sum1 in dic or sum1 == 0:
            return True
        else:
            dic[sum1] = 1
            
    return False

arr = [4, 2, -3, 1, 6]
n = len(arr)
print(zeroSum(arr,n))
