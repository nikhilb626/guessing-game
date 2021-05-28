n=18

guess_num=1

print("\t\t\t..................THE GUESSING GAME....................\t\t\t\t\t")
while guess_num<=10:
    inp=int(input("guess the number:"))
    if inp>n:
        print("guess smaller number")
        print("number of guess left is",10-guess_num)

        guess_num+=1
    elif inp<n:
        print("guess greater number")
        print("number of guess left is",10-guess_num)

        guess_num+=1
    else:
        print("you won")
        print(guess_num,"number of guess took")
        break
    if guess_num>10:
        break
print("***********game over***********")
