class Calculator:
    length = ""

    def __init__(self,len):
        self.length = len

    def cube(self):
        return self.length**3
    def square(self):
        return self.length**2
    def sqrt(self):
        return self.length**(0.5)
    
tejas = Calculator(int(input("Enter Your Number:- ")))
print(tejas.cube())
print(tejas.square())
print(tejas.sqrt())