from random import *
print("Welcome to this Game\n")
print(f'''About this Game:
            This game is played between you and computer :=
                In this game, you can choose any one from
                Rock, Paper and Scissor and same can be done by computer itself\n''')
print(f'''Rules :
        Choice A (You)    Choice B (Computer)      Result
        ---------------------------------------------------
            Paper               Rock               You Won
            Rock              Scissor              You Won
            Scissor             paper              You Won \n''')
input("Enter Your Name: \n")
A='y'
while A=='y':
    lst=['Rock','Paper','Scissor']
    b=choice(lst)
    a=int(input(f'''Enter Your Choice:=
                    Press 1 for Rock
                    Press 2 for Paper
                    Press 3 for Scissor\n'''))
    match a:
        case 1:
            a='Rock'
        case 2:
            a='Paper'
        case 3:
            a='Scissor'
    if (a=='Rock' and b=='Scissor') or (a=='Paper' and b=='Rock') or (a=='Scissor' and b=='Paper'):
        print("Congratulations! You Won the Game")
    elif a==b:
        print("Game is Tie")
    else:
        print("You lose the Game")
    A=input(f'''Do you want to play again ?
        if yes then press \'y\' if no press \'n\'\n''')
print("Game End")