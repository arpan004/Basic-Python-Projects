from random import *
print(f'''Welcome:=
About:-
    This is a Game of Dice Where you can role a pair of Dice and get result\n''')
a=input(f'''To Role a pair of Dice Press \'y\'
To end this Game Press \'n\'\n''')
while a=='y':
    dice1=randint(1,6)
    dice2=randint(1,6)
    print("Your result is",dice1,dice2,"\n")
    a=input(f'''Do you want to Roll the dice Again then Press \'y\'
    if you want to end this Game then Press \'n\'\n''')
print("Game End:))")