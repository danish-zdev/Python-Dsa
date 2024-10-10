
def twoSum(arr):

    # for i in range(n):
    #     for j in range(i+1,n):
    #         if arr[i] + arr[j] == target:
    #             # return arr[i], arr[j]
    #             print(arr[i],arr[j])
    # print('Pair not found')

    dic={}
    for i in arr:
        if x-i in dic:
            return True
        dic[i]=1
    return False
# 		arr.sort()
# 		start = 0
# 		end = n-1
# 		sum1 =0
# 		while start<end:
# 		    sum1 = arr[start] + arr[end]
# 	        if sum1 == x:
# 	            return "YES"
# 	        elif sum1>x:
# 	            end-=1
# 	        else:
# 	            start+=1
# 		return "NO" 

arr = [1,3,16,5,9,20,29]
n = len(arr)
x = 25
print(twoSum(arr))
