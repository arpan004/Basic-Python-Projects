from random import *
print("Welcome to this Game\n")
print(f'''About this Game:
            This is a Hangman Game in which A row of dashes represents the word to guess.
            If you guess a letter in the word, the script writes it in all its correct positions.\n''')
print(f'''Rules of this game :
       With each wrong guess a hangman design will begin on your screen
       and if the hangman designed is completed that means you don't guess the correct word and You loss the game.\n''')
print("So, the game is very intersting. So Let's Start the game:-\n")
def error(e):
    match e:
        case 1:
            print("Ohh! You Guessed the wrong word")
            print(f'''
        +-----+
        O     |
              |
              |
        ''')
        case 2:
            print("Ohh! You again Guessed the wrong word")
            print(f'''
        +-----+
        O     |
        |     |
              |
        ''')
        case 3:
            print("Ohh! You again Guessed the wrong word")
            print(f'''
        +-----+
        O     |
        |\    |
              |
        ''')
        case 4:
            print("Ohh! You again Guessed the wrong word")
            print(f'''
        +-----+
        O     |
       /|\    |
              |
        ''')
        case 5:
            print("Ohh! You again Guessed the wrong word")
            print(f'''
        +-----+
        O     |
       /|\    |
       /      |
        ''')
        case 6:
            print("Ohh! You again Guessed the wrong word")
            print(f'''
        +-----+
        O     |
       /|\    |
       / \    |
        ''')
            print("Ohh! You loss the Game")
input("Enter Your Name: \n")
A='y'
while A=='y':
    e=0
    c=0
    list=[]
    lst=['Box','Tiger','Lion','Fox','Python','College']
    letter=choice(lst)
    print("Word You Want to guess:-")
    dashes=(["_ " for i in letter])
    print(*dashes)
    while e!=6 and c!=len(letter):
        gword=input("Enter Your guessed character\n")
        if gword in letter:
            i=letter.index(gword)
            letter=letter.replace(gword,'/',1)
            dashes.insert(i,gword)
            dashes.pop(i+1)
            print(*dashes)
            c+=1
        else:
            e+=1
            error(e)
            if e!=6:
                print(*dashes)
    if c==len(letter):
        print("Congratulations! You Guessed the Correct Word and You won the Game")
    A=input(f'''Do you want to play again ?
        if yes then press \'y\' if no press \'n\'\n''')
print("Game End")