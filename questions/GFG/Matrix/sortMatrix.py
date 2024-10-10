def sortedMatrix(N,Mat):
    #code here
    ans = []
    for row in Mat:
        for i in row:
            ans.append(i)
    ans.sort()
    k = 0
    for i in range(N):
        for j in range(N):
            Mat[i][j] = ans[k]
            k+=1
    return Mat

Mat=[[10,20,30,40],
[15,25,35,45], 
[27,29,37,48], 
[32,33,39,50]]

N=len(Mat)

print(sortedMatrix(N,Mat))