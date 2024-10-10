class Employee:
    name = "Harry"
    language = "Python" #class attribute
    salary = 1200
    # drunder methods are called automatically
    # __"name"__ are called drunder methods
    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Created an object!!")

    
    # while running a function please give an argument named self
    def getInfo(self):
        print(f"The name of Employee is {self.name} and Salary is {self.salary}")
    # When you dont want the whole object to be passed then staticmethod is used
    @staticmethod
    def greet():
        print("Good Morning!")

tejas = Employee("Tejas",1000000,"Cpp")

tejas.getInfo()
tejas.greet()


# constructor is called even if not not called in main program
# it is called when an object is created




