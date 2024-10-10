def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
n = 10
print(fib(n))
for i in range(n):
    print(fib(i), end=" ")



# def fibonacci(n):
#     a = 0
#     b = 1
#     while b < n:
#         print(b, end= " ")
#         a, b = b, a + b

# fibonacci(10)


a = 1
for i in range(10):
    print(a, end= " ")
    i, a = a, a+i
