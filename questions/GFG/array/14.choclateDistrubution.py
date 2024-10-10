def findMinDiff(A,N,M):

    # code here
    i = 0
    j = M-1
    d = 100000000
    A.sort()
    while j<N:
        d = min(d, A[j]-A[i])
        j+=1
        i+=1
    return d  

M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]  
N = len(A)
print(findMinDiff(A,N,M))