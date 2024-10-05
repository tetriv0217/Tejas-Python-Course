# dictionary is a collection of key-value pairs

# empty dictionary

d = {}

print(type(d))

# Properties of pyhton dictionary
''' 
It is unordered
It is mutable
It is indexed
Cannot cocntain duplicate keys.
'''

marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23
}

print(f"{marks} \n {type(marks)}")

print(marks["Harry"])
data = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23,
    "list" : [1,2,3,5]
}

print(data["list"])

data["list"] = 1001
print(data["list"])

# You can store any value pairs

marks2 = {
    0 : 1,
    1 : 2
}

print(marks2[0])
print(marks2[1])