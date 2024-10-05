''' 
Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up! 
'''

dictionary = {
    "Kaam" : "Work",
    "Kursi" : "Chair",
    "Hasna" : "Laugh",
}

word= input("Enter Your Hindi word : - ")

print(f"Your English word for {word} is {dictionary[word]}")

