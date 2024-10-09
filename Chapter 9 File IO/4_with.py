f = open("Chapter 9 File IO/sample_text.txt")

print(f.read())

f.close()

# when you read f.close is important

# however with "with" you dont have to close the file it will automatically close


with open("Chapter 9 File IO/sample_text.txt") as f:
    print(f.read())

# with "with" you dont have to explicitly close the file

