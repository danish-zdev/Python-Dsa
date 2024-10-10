



def weightedUniformStrings(s, queries):
    
    a=set()
    w=0
    for c in range(len(s)):
        if s[c]==s[c-1] and c>0:
            w+=ord(s[c])-ord('a')+1
        else:
            w=ord(s[c])-ord('a')+1
        a.add(w)
    return['Yes' if c else 'No' for c in map(lambda x:x in a,queries)]

s = 'abbcccdddd'
queries = [1,7,5,4,15]

print(weightedUniformStrings(s, queries))


    # acode = ord('a')
    # dsvalues, ri = set(), 1
    # for i, c in enumerate(s):
    #     if i == 0 or s[i-1] != c:
    #         ri = 1
    #     else:
    #         ri += 1
    #     dsvalues.add(ri * (1 + ord(c) - acode))

    # return ("Yes" if q in dsvalues else "No" for q in queries)