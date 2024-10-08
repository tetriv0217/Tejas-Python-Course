n = int(input())

for i in range(0,n):
    if(i == 0 or i == n-1):
        for j in range(0,n):
            print("*",end="")
    else:
        print("*",end="")
        for j in range(1,n-1):
            print(" ",end="")
        print("*",end="")
    print()

