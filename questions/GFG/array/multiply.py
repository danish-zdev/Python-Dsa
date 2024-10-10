lst = [1,5,7,9,10,11]
c=lst[0]
print(c)
for i  in range(0,len(lst)-1):
    c=lst[i]*lst[i+1]
    print(c)
# x=[lst[i]*lst[i+1] for i  in range(0,len(lst)-1) ]


# red = [i*j for i, j in zip(lst, lst[1:])]
# print(red)
# print(x)
    