def power(N,R):
    #Your code here
    mod = 1000000007
    
    
    if N==0: return 0
    if R==0: return 1

    return (N%mod *(power(N,R-1)%mod))%mod
     
    # *****save space comlexity ******
    # if R%2 == 0:
    #     ans = power(N,R/2)
    #     return (ans%mod * ans%mod) % mod
    # else:
    #     ans = power(N,(R-1)/2)
    #     return (ans%mod * ans%mod * N%mod) % mod

                
N = 12
R = 21
print(power(N,R))