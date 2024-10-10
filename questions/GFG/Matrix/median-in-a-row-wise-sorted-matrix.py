def median(matrix, R, C):
    #code here 
    lis=[]

    for i in range(R):
        lis+=matrix[i]
    lis.sort()
    return lis[len(lis)//2]
    
# 	lst = []
# 	for i in matrix:
# 	    for j in matrix:
# 	       lst.append(j)
# 	return (len(lst)+1)//2  


M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

R = len(M)
C = len(M[0])
# Output: 5
print(median(M, R, C))