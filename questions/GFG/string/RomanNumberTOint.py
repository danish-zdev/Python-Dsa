def romanToDecimal(s): 
    # code here
    dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sum=0
    # for i in range(len(S)):
    #         if i==len(S)-1 or dic[S[i]]>=dic[S[i+1]]:
    #             sum+=dic[S[i]]    
    #         else:
    #             sum-=dic[S[i]]

    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    for i in s:
        sum += dic[i]
    return sum

    # s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    # return sum(map(lambda x: roman[x], s))

    # number=0
    # for i in range(len(s)-1):
    #     if roman[s[i]] < roman[s[(i+1)]]:
    #         number-=roman[s[i]]
    #     else:
    #         number+=roman[s[i]]
    # return number+roman[s[-1]]

s = 'IVX'

print(romanToDecimal(s))