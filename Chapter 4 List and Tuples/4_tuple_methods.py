a = (1,123,23,45,36,56,7,1234,"Rohan","Aakash","Shivam")

# error
# a[0] = 12

print(a)

print(a.count(45))


print(a.index(45))# give first occurence in a tuple

b = (1,2)
print(b*3) # repeats the element

# in , membership operator
print(2 in b)
print(100 in b)

print(max(b))
print(min(b))

print(len(a))

# unpacking
first,second = b

print(first,second)


sliced = a[1:4]
print(sliced)