def _sum(arr, n):
    # code here
    if n == 0:
        return 0
    elif(n==1):
        return arr[0]   
    else:
        return arr[n-1]+_sum(arr,n-1)
    


arr = [1, 2, 3, 4]
n = len(arr)

print(_sum(arr, n))
# Output: 10
# Explanation: 1 + 2 + 3 + 4 = 10.    

    #    _sum([1,2,3,4], 4)
    #        /          |        \
    #  4 + _sum([1,2,3], 3)   |
    #                  /   |      \
    #          3 + _sum([1,2], 2) |
    #                     /  |      \
    #             2 + _sum([1], 1) |
    #                         |
    #                         1