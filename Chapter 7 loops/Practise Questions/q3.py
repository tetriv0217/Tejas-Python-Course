n = int(input())

flag = False

for i in range(2,int(n**0.5)+1):
    if(n%i == 0):
        flag = True
        break

if flag == True:
    print(f"{n} is not prime")
else:
    print(f"{n} is prime")
    


