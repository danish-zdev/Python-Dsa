# missing number in a given integer array of 1 to 100

def MissingNumber_1to100(arr, num):

    # MissingNumber =[]
    # for i in range(100):
    #     if i not in arr:
    #        MissingNumber.append(i)
    # print(MissingNumber)

    # sum = n*(n+1)//2
    # Osum = 1
    # for i in range(n):
    #     Osum = i+Osum
        
    # return sum-Osum   
    
    arr.sort()
    num = 1
    for i in range(n):
        if arr[i] == num and arr[i]>=1:
            num+=1
    return num   

    # array.sort()
    # for i in range(1,n+1):
    #     if i == n :
    #         return i
    #     if i!=array[i-1]:
    #         return i 


# arr = [1,2,3,4,5,6,7,9,10]
# arr = [1,2,3,3,11,6,7,9,10,13]
arr = [0,-10,1,3,-20]

n = len(arr)

# MissingNumber2 = [item for item in range(n) if item not in arr]
# print("methotd 2--------", MissingNumber2)

print(MissingNumber_1to100(arr, n))



    # code here
    # array.sort()
    # c=0
    # if(n==2):
    #     c=array[0]+1
    #     return c
    # for i in range(0,len(array)-1):
    #     if array[i]+1 not in array:
    #         c=array[i]+1
    #         break
    #         # print(array[i]+1)
    # return c 
    
