def sumOfNaturalNums(n):
    if(n == 1):
        return 1
    return n+sumOfNaturalNums(n-1)

print(sumOfNaturalNums(4))