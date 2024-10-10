# def LinearSearch(key, arr):
#     n = len(arr)
#     for i in range(n):
#         if key == arr[i]:
#             print("Element has found at index", i)
#             break
#     else:   
#         print("Element not found")
    

# arr = [9, 2, 4, 0, 45, 0]
# key = 0

# LinearSearch(key, arr)



def LinearSearch(key, arr):
    n = len(arr)
    Lst = []
    
    flag = False
    for i in range(n):
        if key == arr[i]:
            flag = True
            Lst.append(i)

    if flag == True:
        for i in Lst:
           print("Element found at index:", i)
    else:
        print("key not found")




arr = [9, 2, 4, 0, 45, 0]
key = 0

LinearSearch(key, arr)