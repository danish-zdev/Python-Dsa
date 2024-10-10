def cube(x):
    return x*x

lst = [1,5,2,3,4]

# out = list(map(cube, lst))
##or
map1 = list(map(lambda x: x*x, lst))
print("Map ->", map1)

filter1 = list(filter(lambda x:x>1, lst))
print("Filter ->", filter1)


from functools import reduce
def sum1(x,y):
    return x+y
# reduce1 = reduce(sum1, lst)
reduce1 = reduce(lambda x,y:x+y, lst)


print(reduce1)

