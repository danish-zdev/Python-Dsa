def spirallyTraverse(matrix, r, c): 
    # code here 

    start_row = 0
    end_row  = r-1
    start_col = 0
    end_col = c-1
    spiral_order = []
    
    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col,end_col):
            spiral_order.append(matrix[start_row][i])

        for i in range(start_row,end_row+1):
            spiral_order.append(matrix[i][end_col])

        for i in range(end_col-1,start_col,-1):
            if start_row == end_row:
                break
            spiral_order.append(matrix[end_row][i])

        for i in range(end_row,start_row,-1):
            if start_col == end_col:
                break
            spiral_order.append(matrix[i][start_col])

        start_row += 1
        end_row -= 1
        
        start_col += 1
        end_col -= 1

    return spiral_order


matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16]]


r = len(matrix)
c = len(matrix)
print(r,c)
print(spirallyTraverse(matrix, r, c))
