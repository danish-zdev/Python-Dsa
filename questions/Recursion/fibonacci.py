def nthFibonacci(n):
    
    # code here 
    dp = [-1] * 1001
    mod = 1000000007

    if dp[n] != -1:
        return dp[n]
    elif n <= 1:
        dp[n] = n
        return n

    else:
        dp[n] = (nthFibonacci(n-1) + nthFibonacci(n-2)) % mod
        return dp[n]

n= 3
print(nthFibonacci(n))            

  
    
# f = [0, 1]
# for i in range(2, n+1):
#     f.append(f[i-1] + f[i-2])
# return f[n]%1000000007



#bottom to top appraoch
# def fibnum1(x):
#     arr=[0,1]
#     if x in arr:
#         return x
#     for i in range(2,x+1):
#         arr.append(arr[i-1]+arr[i-2])
#     return arr[-1]
# return fibnum1(n)



# # Check if n is 0 or 1, return n in that case
# if n < 2:
#     return n

# # Initialize variables for the first two Fibonacci numbers
# prev1, prev2 = 0, 1

# # Loop through the remaining numbers and calculate the next Fibonacci number
# for _ in range(n-1):
#     prev1, prev2 = prev2, prev1 + prev2

# # Return the nth Fibonacci number
# return prev2


