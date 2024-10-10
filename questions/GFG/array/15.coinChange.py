
def count( coins, N, Sum):
    # code here 
    dp = [1] + [0] * Sum
    for i in coins:
        for j in range(i, Sum + 1):
            dp[j] += dp[j - i]
    return dp[-1]   

Sum = 10 
coins = [2,5,3,6]
N = len(coins)

print(count( coins, N, Sum))
# Explanation: Five Possible ways are:
# {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} 
# and {5,5}.                    