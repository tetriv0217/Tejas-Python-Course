with open("Chapter 9 File IO/Chapter 9 PS/q6/sample.txt","r") as f:
    content = f.readline()
    while content:
        if("Python" in content or "python" in content):
            print("Python is present")
            break
        content = f.readline()
    else:
        print("Python not present")