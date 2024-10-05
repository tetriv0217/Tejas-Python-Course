string = input("Enter Your name:- ")

ls = ["Rohan","Mohan","Harry","Larry","Tejas"]

if (string not in ls):
    print(f"{string} not present in the list")
else :
    print(f"Present at index {ls.index(string)}")