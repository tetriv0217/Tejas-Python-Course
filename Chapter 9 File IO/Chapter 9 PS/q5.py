ls = ["Donkey","Pussy","Fuck"]
with open("Chapter 9 File IO/Chapter 9 PS/q4_donkey.txt","r+") as f:
    content = f.read()
    for word in ls:
        content = content.replace(word,"#"*len(word)).replace(word.lower(),"#"*len(word))
    f.seek(0)
    f.write(content)
    f.truncate()