

def count0s1s(arr,n):
    d = {}
    sum1 = 0
    ans = 0
    d[0] = 1

    for i in range(n):
        if arr[i] == 0:
            sum1 -= 1
        else:
            sum1 += 1
            
        if sum1 in d:
            ans += d[sum1]
            d[sum1] += 1
        else:
            d[sum1] = 1

    return ans

arr = [1, 0, 0, 1, 0, 1, 1]
n = len(arr)
print(count0s1s(arr,n))