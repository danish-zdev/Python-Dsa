def minimumPlatform(n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        count = 0
        ans = 0
        
        i,j = 0,0 
        while i < n:
            if arr[i] <= dep[j]:
                count += 1
                ans = max(ans,count)
                i+=1
            else:
                count-=1
                j+=1
                
        return ans 


arr =[1900, 1940, 1950, 1100, 1500, 1800]
dep =[1910, 2200, 2120, 1130, 1900, 2000]            
n= len(arr)

print(minimumPlatform(n,arr,dep))