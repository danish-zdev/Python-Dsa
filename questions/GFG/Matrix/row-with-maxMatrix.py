def rowWithMax1s(arr, n, m):
    # code here
    # for i in range(m):
    #     for j in range(n):
    #         if(arr[j][i]==1):
    #             return j
    # return -1

    max1=0
    max_i=-1
    for i in range(n):
        max_sum=sum(arr[i])
        if(max_sum>max1):
            max1=max_sum
            max_i=i
    return max_i


arr= [[0, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]]

n = len(arr)
m = len(arr)
print(rowWithMax1s(arr, n, m))