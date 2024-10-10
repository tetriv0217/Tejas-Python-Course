def game():
    score = int(input("Enter your score:- "))
    with open("Chapter 9 File IO/Chapter 9 PS/Hi-score.txt","r+") as f:
        data = f.read()
        if data == "":
            f.write(str(score))
        else:
            if(int(data)<score):
                print("You created a new high score")
                f.seek(0)
                f.write(str(score))
                f.truncate()
            else:
                print(f"the preious highscore is {data}")

game()
