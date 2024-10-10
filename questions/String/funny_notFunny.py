def funnyString(s):
    # Write your code here
    r=s[::-1]
    l1=[abs((ord(s[i])-ord(s[i+1]))) for i in range(0,len(s)-1)]
    l2=[abs((ord(r[i])-ord(r[i+1]))) for i in range(0,len(r)-1)]
    print(l1,l2)
    if l1==l2:
        return "Funny"
    else:
        return "Not Funny"
    
# s = 'lmop'
# s = 'ponml'
s =  'bcxz'
print(funnyString(s))