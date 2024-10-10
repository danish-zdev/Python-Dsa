def Search(arr, start, end, key):
    
    if start > end:
        return -1

    mid = start + (start + end) // 2

    if arr[start] <= arr[mid]:
        if key >= arr[start] and key <= arr[mid]:
            return Search(arr, mid+1, end, key)
        return Search(arr, start, mid-1, key)   
        
    
