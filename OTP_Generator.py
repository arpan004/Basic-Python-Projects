from random import *
print(f'''Welcome:=
        This is an OTP Generator\n''')
a=input(f'''To Generate the OTP Press \'y\'
To end this Program Press \'n\'\n''')
while a=='y':
    otp=randrange(100000,999999)
    print("Your 6 digit OTP is",otp,"\n")
    a=input(f'''Do you want to Generate the OTP Again then Press \'y\'
    if you want to end this Program then Press \'n\'\n''')
print("Program End")