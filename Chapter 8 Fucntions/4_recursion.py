def facto(n):
    if(n <= 1):
        return 1
    return n*facto(n-1)

print(f"{6}! is {facto(5)}")