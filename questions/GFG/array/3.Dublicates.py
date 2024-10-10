

def dublicates(arr):
    # lst = []
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if arr[i] != arr[j]:
    #             lst.append(arr[j])
    #         break
    #             # print(arr[j])
    # print(lst)

    from collections import defaultdict
    mp= defaultdict(int)
    x=0
    for i in arr:
        mp[i]+=1
        if mp[i]==1:
            arr[x]=i
            x+=1
    return len(mp)

    
    




arr = [2,3,3,0,4,2,5,7,8,9,4]
n = len(arr)    
print(dublicates(arr))
    
