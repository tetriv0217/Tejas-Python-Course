'''
Write a program to input eight numbers from the user and display all the unique 
numbers (once).
'''

s = set()

s.add(int(input("Enter your numbers:- ")))
s.add(int(input("Enter your numbers:- ")))
s.add(int(input("Enter your numbers:- ")))
s.add(int(input("Enter your numbers:- ")))
s.add(int(input("Enter your numbers:- ")))
s.add(int(input("Enter your numbers:- ")))
s.add(int(input("Enter your numbers:- ")))
s.add(int(input("Enter your numbers:- ")))

print(f"Your numbers without repetition is {s}")
