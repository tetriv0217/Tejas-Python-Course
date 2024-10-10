with open("Chapter 9 File IO/Chapter 9 PS/q1_poems.txt","r") as f:
    data = f.read()
    if(data.find("Twinkle") != -1 or data.find("twinkle") != -1 ):
        print(data)
        print("Twinkle is present")
    else:
        print(data)
        print("Not Present")