def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    # f = 1
    # for i in range(1,n+1):
    #     f = f*i
    # return f

print(factorial(5))
