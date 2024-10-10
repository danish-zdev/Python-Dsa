# d = {1:"A", 2:"B", 3:"C", 4:"D"}

# i = "DC"
# size = len(i)


# for k, v in d.items():
#     if i in v:
#         print(i[0])
#         # for j in range(int(size)):
#         #     print(j.values())
#             # for k in range(int(j+1, size)):
#             #     print(int(i[j]*i[k]))


# lst = [[1,3],
#        [4,6,7],
#        [23,"asad", 1.23]
#        

# print(lst[1][0])

# for i in range(0,6):
#     for j in range(i, 6):
#         print("*", end=" ")
#     print() 
# for i in range(0,6):
#     for j in range(i, 6):
#         print("*", end=" ")
#     print()       


def demo():
    nums1 = [1,2]
    nums2 = [3,4]

    l = nums1+nums2
    l.sort()
    size = len(l)
    # print(l)

    o = size//2

    if size % 2== 0:
        return((l[o]+l[o-1])/2)        
    else:  
        return(o+1)

print(demo())

# if 5 % 2== 0:
#     print("Even")    
# else:
#     print("Odee")
    




    