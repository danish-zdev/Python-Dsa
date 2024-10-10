def calculateSpan(a,n):
    #code here
    stack = []
    result = []
    for item in a: 
        count = 1
        while stack and item >= stack[-1][0]:
            count += stack.pop()[1]
        stack.append((item, count))
        result.append(count)
    return result

a = [100, 80, 60, 70, 60, 75, 85]
n = len(a)

print(calculateSpan(a,n))