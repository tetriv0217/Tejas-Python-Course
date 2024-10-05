s = {1,2,3,4,5,6,54,"Harry"}


print(s,type(s))

s.add("teajsa")

print(s)


print(len(s))

# s.remove("123")# gives error if argument not present in set
s.remove("teajsa")# gives error if argument not present in set
print(s)

# s.pop() # removes an arbitrary element
# print(s)

# union and intersection

s1 = {1,2,3,4,5}
s2 = {12,435,56,78,1,2}

print(s1.union(s2))
print(s1.intersection(s2))

# s1.clear()
# print(s1) # set()

print(s1.issuperset({1,2}))
print({1,2}.issubset(s1))