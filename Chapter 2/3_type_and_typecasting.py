a = 10
b = 10.2
c = "10"
d = True
e = None

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'str'>
print(type(d)) # <class 'bool'>
print(type(e)) # <class 'NoneType'>


a = 100
b = float(a) # Type casting

print(b)
print(type(b))

c = "121"
d = int(c)

print(d)

e = ""
f = bool(e)
print(f) # false
e = " "
f = bool(e)
print(f) # true

g = None
# h = int(g) # error
h = str(g)
print(h) # None
print(type(h)) # None
