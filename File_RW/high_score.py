score = str(input("Please enter your score: "))
name = input("Please enter your name: ")

with open("score.txt", "w") as f:
    f.write(score)
    f.write(" \n")
    f.write(name)
