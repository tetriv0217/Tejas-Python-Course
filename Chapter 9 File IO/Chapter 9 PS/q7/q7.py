with open("Chapter 9 File IO/Chapter 9 PS/q6/sample.txt","r") as f:
    content = f.readline()
    line = 1
    while content:
        if("Python" in content or "python" in content):
            print(f"Python is present in line {line}")
            break
        content = f.readline()
        line+=1
    else:
        print("Python not present")