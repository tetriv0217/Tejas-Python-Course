class Employee:
    name = "Harry"
    language = "Python" #class attribute
    salary = 1200

harry = Employee()
harry.name = "Larry" #instance attribute
print(harry.name,harry.language)