import heapq

def topKFrequent(nums, k):
    d = {}
    ans = []
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for key, val in d.items():
        if len(ans) < k:
            heapq.heappush(ans, [val, key])  
        else:
            heapq.heappushpop(ans, [val, key]) 

    return [key for value, key in ans]     


nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))


# Output: [1,2]