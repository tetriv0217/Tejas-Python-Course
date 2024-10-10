with open("Chapter 9 File IO/Chapter 9 PS/q10/erase.txt","r+") as f:
    f.seek(0)
    f.truncate()
    print("Erase done")
    # pass