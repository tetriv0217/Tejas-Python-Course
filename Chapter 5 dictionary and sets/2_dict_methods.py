marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23
}

print(marks.items())# dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 23)])
print(marks.keys())# dict_keys(['Harry', 'Shubham', 'Rohan'])

marks.update({"Harry" : 99,"Renuka" : 90})# here renuka is not present so it will get added to dictionary

print(marks)
# get gives None if value not present and marks[key] will give error if not present
print(marks.get("Harry2"))# None
# print(marks["Harry2"])# error

print(marks.get("Harry"))# 

val = marks.pop("Shahi",100)# pop takes two arguments, 1 is key and 2nd is default value, what default value does that if key is not present then the default value is printed
print(val)