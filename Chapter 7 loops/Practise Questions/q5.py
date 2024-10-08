n = int(input())

for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
    for j in range(0,n-i-1):
        print(" ",end="")
    print()


for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()