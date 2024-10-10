class Employee:
    name = "Harry"
    language = "Python" #class attribute
    salary = 1200
    # while running a function please give an argument named self
    def getInfo(self):
        print(f"The name of Employee is {self.name} and Salary is {self.salary}")
    # When you dont want the whole object to be passed then staticmethod is used
    @staticmethod
    def greet():
        print("Good Morning!")

harry = Employee()
harry.name = "Larry" #instance attribute
print(harry.name,harry.language)
harry.getInfo()
harry.greet()
# harry.getInfo() == Employee.getInfo(harry)
#since it takes one argument we have to give self as argument
# Employee.getInfo(harry)

