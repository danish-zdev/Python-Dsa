def searchMatrix(matrix, target):
    temp=[]
    for i in matrix:
        for j in i:
            if target == j:
                return True
    else:
        return False

    # row = len(matrix)
    # col = len(matrix[0])
    # low = 0
    # high = row * col - 1
    
    # while low <= high:
    #     mid = (low + high) // 2
    #     if matrix[mid // col][mid % col] == target:
    #         return True
    #     elif matrix[mid // col][mid % col] < target:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
            
    # return False
target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix, target))