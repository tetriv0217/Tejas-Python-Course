# with open("Chapter 9 File IO/Chapter 9 PS/q9/compare1.txt") as file1:
#     with open("Chapter 9 File IO/Chapter 9 PS/q9/compare2.txt") as file2:
#         data1 = file1.read()
#         data2 = file2.read()
#         if(data1 == data2):
#             print("The Content is similar")
#         else:
#             print("Not Similar")
    
with open("Chapter 9 File IO/Chapter 9 PS/q9/compare1.txt") as file1:
    with open("Chapter 9 File IO/Chapter 9 PS/q9/compare2.txt") as file2:
        for line1,line2 in zip(file1,file2):
            if(line1 != line2):
                print("The content is not similar")
                break
        else:
            if(file1.read() == "" and file2.read() == ""):
                print(f"The Contents are similar!!")
            else:
                print("Not similar")