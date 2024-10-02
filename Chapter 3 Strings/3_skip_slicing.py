a = "0123456789"

print(a[0:9])
print(a[0:9:2])#02468
# 0 1 2 3 4 5 6 7 8
# T S T S T S T S T

# this 2 means take the second character
print(a[0:9:3]) #036
# 0 1 2 3 4 5 6 7 8
# T S S T S S T S S

print(a[0::3]) #0369  equivalent to 0:len-1:3
