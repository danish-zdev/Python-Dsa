import abc


def countBitsFlip(a,b):
    ##Your code here
    count = 0
    c = a^b
    while(c):
        c = c&(c-1)
        count +=1
    return count    

a = 10
b = 20

print(countBitsFlip(a,b))



# Input: abc = 10, B = 20
# Output: 4
# Explanation:
# A  = 01010
# B  = 10100
# As we can see, the bits of A that need 
# to be flipped are 01010. If we flip 
# these bits, we get 10100, which is B.