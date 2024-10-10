def maxProfit(prices):
    
    # left = 0 #Buy
    # right = 1 #Sell
    # max_profit = 0
    # while right < len(prices):
    #     currentProfit = prices[right] - prices[left] #our current Profit
    #     if prices[left] < prices[right]:
    #         max_profit =max(currentProfit,max_profit)
    #     else:
    #         left = right
    #     right += 1
    # return max_profit


    curr = 0
    mp = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            # mp += prices[i+1] - prices[i]
            curr = prices[i+1] - prices[i]
            mp = max(curr, mp)

# prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
print(maxProfit(prices))