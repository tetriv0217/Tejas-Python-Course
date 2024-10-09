'''
How to read a file
'''

f = open("Chapter 9 File IO/sample_text.txt","r")
#Open takes two inputs number one is file name and second is read or write mode, by default the mode is read
data = f.read()
print(data)
f.close()