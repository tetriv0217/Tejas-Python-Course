f = open("Chapter 9 File IO/sample_text.txt")

# readline gives a list of all the lines with a \n appended
# lines = f.readlines()
# print(lines,type(lines))


# readline returns a string of first line and cursor is at second line
# line1 = f.readline()
# print(line1,type(line1))
# line2 = f.readline()
# print(line2,type(line2))
# line3 = f.readline()
# print(line3,type(line3))
# line4 = f.readline()
# print(line4=="",type(line4))

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

