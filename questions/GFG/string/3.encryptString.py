def encryptString(S):
    # code here
    count=0
    temp=[]
    result=''
    for i in range(len(S)):
        if i<len(S)-1 and S[i]==S[i+1]:
            count+=1
        else:
            temp.append(str(hex(count+1))[2:]+S[i])
            count=0
    for j in range(len(temp)-1,-1,-1):
        result+=temp[j]
    return result


    # s=list(S)
    # d={}
    # for i in range(len(s)):
    #     if s[i] in d.keys():
    #         d[s[i]]+=1
    #     else:
    #         d[s[i]]=1
    # for k,v in d.items():
    #     if(d[k]==10):
    #         d[k]="a"
    #     if(d[k]==11):
    #         d[k]="b"
    #     if(d[k]==12):
    #         d[k]="c"
    #     if(d[k]==13):
    #         d[k]="d"
    #     if(d[k]==14):
    #         d[k]="e"
    #     if(d[k]==15):
    #         d[k]="f"
    # arr=[]
    # for k,v in d.items():
    #     arr.append(k)
    #     arr.append(v)  
    # h=arr.reverse()
    # listToStr = ''.join(map(str, arr))
    # return listToStr

# S = "aaaaaaaaaaa"
S = "abc"

# SS = "abc"
# Output:
# 1c1b1a
encryptString(S)    