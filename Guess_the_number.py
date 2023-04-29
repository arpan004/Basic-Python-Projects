from random import *
print("Welcome to this Game\n")
print(f'''About this Game:
                In this game, the computer will guess a random number between 1 to 100 and you will try to guess what number it is.
                The game ends when you guess the correct number but you only get 10 chances max. to guess the correct number.\n''')
input("Enter Your Name: \n")
a='y'
while a=='y':
    num=randint(1,100)
    score=10
    chance=0
    for i in range(10):
        n=int(input("Guess the number\n"))
        chance+=1
        if n==num:
            print("Congratulations! you can guess the number in",chance,"chances")
            print("Your Score is",score)
            break
        else:
            if chance==10:
                print("You loss the Game")
                break
            print("Wrong guess Now again",end=" ")
            score-=1
    a=input(f'''Do you want to play again ?
        if yes then press \'y\' if no press \'n\'\n''')
print("Game End")