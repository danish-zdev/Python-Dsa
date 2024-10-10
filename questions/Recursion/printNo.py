def printNos(N):
    #Your code here
    if N == 0: return 0
    else:
        printNos(N-1)
        print(N, end =" ")
N = 10
printNos(N)        