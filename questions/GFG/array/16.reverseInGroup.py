def reverseInGroups(arr, N, K):
    # code here
    # arr= [1,2,3,4,5]
    # N = len(arr)
    # K = 3

    # for i in range(0, N, K):
    #     arr[i:i+K] = arr[i:i+K][::-1]
    # return arr

    for i in range(0, N, K):
            left = i
            right = min(i + K - 1, N - 1)
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
    return arr

arr= [1,2,3,4,5]
N = len(arr)
K = 3
print(reverseInGroups(arr, N, K))

# Output: 3 2 1 5 4
# Explanation: First group consists of elements
# 1, 2, 3. Second group consists of 4,5.        
