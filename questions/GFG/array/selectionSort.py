
def selectionSort(arr):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr             



arr = [4,1,3,0,9,5]
n = len(arr)

print(selectionSort(arr))