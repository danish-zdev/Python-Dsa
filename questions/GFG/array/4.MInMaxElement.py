def minmax(arr):

    minn = arr[0]
    maxx = arr[0]
    for i in range(n):
        if arr[i] < minn:
            minn  = arr[i]
            # print(minn)
        if arr[i] > maxx:
            maxx = arr[i]
            # print(maxx)


    print(minn, maxx, "-----------")
arr = [3,4,5,623,31,0,12]
n = len(arr)
minmax(arr)
