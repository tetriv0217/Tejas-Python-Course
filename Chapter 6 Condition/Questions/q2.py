string = input("Enter your text:- ")

if ("Make a lot of money" in string):
    print("The mail is spam")
elif (string.find("buy now") != -1):
    print("The mail is spam")
elif (string.find("subscribe this") != -1):
    print("The mail is spam")
elif (string.find("click this") != -1):
    print("The mail is spam")
else:
    print("Legit mail")