def LargButMinFreq(arr,n):
    
    dicts = {}
    lis = []
    for ar in arr:
        if ar in dicts:
            dicts[ar]+= 1
        else:
            dicts[ar] =  1
    
    min_m = min(dicts.values())
    # print(min_m)
    for frq in dicts:
        if dicts[frq] == min_m:
            lis.append(frq)
    return max(lis)

arr = [3,3,9,7, 1, 9]
n = len(arr)

print(LargButMinFreq(arr, n))