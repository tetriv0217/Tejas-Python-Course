with open("Chapter 9 File IO/Chapter 9 PS/q4_donkey.txt","r+") as f:
    content = f.read()
    updated_content = content.replace("Donkey","#####").replace("donkey","######")
    f.seek(0)
    f.write(updated_content)
    f.truncate()