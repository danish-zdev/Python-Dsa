for i in range(int(input("Enter Number of time print and check sum: "))):
    x,y = map(int,input().split())
    # x, y = int(input())

    x += y 
    if(x>=7):
        print("yes")
    else:
        print("no")