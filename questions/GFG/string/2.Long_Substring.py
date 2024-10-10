def LogSubStr(s):
    n = len(s)

    # for i in range(n):
    #     for j in range(1, n):
    #         if s[0][i] != s[j][i]:
    #             return s[0][:i]

    # return s[0]  

    # res = ''
    # for i in range(len(s[0])):
    #     for j in s:
    #         if i == len(j) or j[i] != s[0][i]:
    #             return res
    #     res += s[0][i]    
        
    # return res 
    # 
    # 
    res = ""
   
    for a in zip(*s):
        print(a)
        if len(set(a)) == 1: 
            
            res += a[0]
        else: 
            return res
    return res 


    # if len(s) == 1:
    #     return s[0]

    # pref=''
    # s.sort()    
    # for i in range(len(s[0])):
    #     if s[0][i] == s[-1][i]:
    #         pref += s[0][i]
    #     else:
    #         break
    # if(len(pref)==0):
    #     return -1
    # return pref   

s= ['flower', 'flow', 'flight']
print(LogSubStr(s))