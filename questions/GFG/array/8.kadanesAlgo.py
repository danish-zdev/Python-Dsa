def maxSubArraySum(arr,N):
    ##Your code here
    
    maxSum = arr[0]
    curSum = 0
    
    for i in range(N):
        curSum = curSum+arr[i]
        if curSum > maxSum:
            maxSum = max(curSum,maxSum)
        if curSum < 0:
            curSum = 0
            
    return maxSum
arr = [-1,-2,-3,-4]
N  = len(arr)

print(maxSubArraySum(arr,N))

# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)

# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.
