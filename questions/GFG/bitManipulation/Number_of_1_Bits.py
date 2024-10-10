def setBits(N):
    # code here
# 		return bin(N).count('1')
    c = 0
    while(N!=0):
        if(N&1 == 1):
            c+=1
        N = N>>1
    return c 
N = 6
print(setBits(N))