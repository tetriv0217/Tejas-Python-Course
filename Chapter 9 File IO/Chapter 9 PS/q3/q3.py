for i in range(2,21):
    with open(f"Chapter 9 File IO/Chapter 9 PS/q3/tables{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")
