
def frequencyCount(arr, N, P):

    # cnt = [0] * max(N, P)
    # for i in range(N):
    #     cnt[arr[i] - 1] += 1
    # for i in range(N):
    #     arr[i] = cnt[i]
    # return arr   

    
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            

    count = 1  # keeps track of counter <=P

    for i in range(N):
        if count <= P and count in d:
            arr[i] = d[count]
            count += 1
        else:
            arr[i] = 0
            count += 1
    return arr




arr = [2, 3, 2, 3, 5]
P = 5
N = len(arr)
# Output:
# 0 2 2 0 1

print(frequencyCount(arr, N, P))

