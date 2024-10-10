def subArraySum(arr, s): 
    #Write your code here
    dict = {}
    mySum = 0
    
    
    for i in range(n):
        mySum = mySum + arr[i]
        
        if mySum == s:
            print("Subarray starts from 0 to",i)
            break
        
        if mySum - s in dict:
            print("Subarray starts from", dict[mySum-s]+1, "to", i)
            break
        
        dict[mySum] = i
          
arr = [1,4,20,3,10,5]
n = len(arr)
s = 33


subArraySum(arr, s)