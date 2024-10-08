n = int(input())

# for i in range(0,n):
#     if(i == 0 or i == n-1):
#         for j in range(0,n):
#             print("*",end="")
#     else:
#         print("*",end="")
#         for j in range(1,n-1):
#             print(" ",end="")
#         print("*",end="")
#     print()

for i in range(1,1+n):
    if(i == 1 or i == n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print()
