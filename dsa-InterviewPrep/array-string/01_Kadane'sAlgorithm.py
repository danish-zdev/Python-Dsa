
# function to find the sum of contiguous subarray with maximum sum.
def maxSubArraySum(arr):
    ##Your code here
    N = len(arr)   
    maxSum = arr[0]
    curSum = 0
    
    for i in range(N):
        curSum = curSum+arr[i]
        if curSum > maxSum:
            maxSum = max(curSum,maxSum)
        if curSum < 0:
            curSum = 0
            
    return maxSum        
            


arr = [1,2, 3, -2, 5]

print(maxSubArraySum(arr))

# For Input: 
# 1 2 3 -2 5
# Your Output: 
# 9
# Expected Output: 
# 9
