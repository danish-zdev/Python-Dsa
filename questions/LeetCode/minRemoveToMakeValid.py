def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """
    stack=[]
    split_str=list(s)
    for i in range(len(s)):
        if s[i]=='(':
            # if current char is '(' then push it to stack
            stack.append(i)
        elif s[i]==')':
            # if current char is ')' then pop top of the stack
            if len(stack) !=0:
                stack.pop()
            else:
                # if our stack is empty then we can't pop so make  current char as ''
                split_str[i]=""
    for i in stack:
        split_str[i]=""
    return '' .join(split_str)

s = "lee(t(c)o)de)"
# s = "a)b(c)d"
# s = "))(("

print(minRemoveToMakeValid(s))