from random import *
from string import *
upper=ascii_uppercase
lower=ascii_lowercase
digit=digits
symbol=punctuation
print(f'''Welcome:=
        This is a Secure Password Generator Tool\n''')
a=input(f'''To Generate the Secure Password Press \'y\'
To end this Program Press \'n\'\n''')
while a=='y':
    lst=[upper,lower,digit,symbol]
    num=randint(8,12)
    pswd=(choices(lst[0],k=num//4)+choices(lst[1],k=num//4)+choices(lst[2],k=num//4)+choices(lst[3],k=num//4))
    shuffle(pswd)
    ps="".join((pswd))
    print(ps)
    a=input(f'''Do you want to Generate the Secure Password Again then Press \'y\'
    if you want to end this Program then Press \'n\'\n''')
print("Program End\nThanks For Using this Program :))")