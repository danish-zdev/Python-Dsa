# def twoSum(nums, target):
#     dic = {}

#     for i, v in enumerate(nums):
#         if(target - v in dic):
#             return dic[target - v], i
#         dic[v] = i   

# nums = [3, 5, 7, 11, 14]
# target = 21
# print(twoSum(nums, target))




def twoSum(nums, target):

    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if target - nums[i] == nums[j]:
                return [i, j]
    return None            
     
nums = [3, 5, 7, 11, 14]
target = 21
print(twoSum(nums, target))

