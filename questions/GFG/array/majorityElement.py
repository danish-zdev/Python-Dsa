def majorityElement(nums):
    # count=0
    # result=0
    # for n in nums:
    #     if count==0:
    #         result=n
    #     if n==result:
    #         count+=1
    #     else:
    #         count-=1
    # return result

    x=len(nums)//2
    y=set(nums)
    for i in y:
        if nums.count(i)>x:
            return i

nums = [0,2,1,1,2,1,3]

print(majorityElement(nums))