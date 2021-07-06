from getpass import getpass
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def txt(name,email,phone,password,con_password):
    if len(name) > 6 and re.match(regex, email) and len(phone) >= 11 and password == con_password and len(password) >= 8:
        print(f"""
-------------------------------------------------------------------
                        Register Successfully
-------------------------------------------------------------------
                        Name: {name}
                        Email: {email}
                        Phone: {phone}
                        Password: Password Protected
*******************************************************************
        Congratulation Your Account Is Successfully Created
*******************************************************************
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Welcome To ABC
                              Thank You
                    Emergency Contact: 0199-860-3947
                 E-Mail: amirhamzashuvokhan@gmail.com
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    else:
        print("""
$---------------------------------------------------------------------------------------------------$
 Please Check Name, Email, Phone Number and Password!
 Name Should Be 6 Char!
 Email Should Be Valid! (Example: abcadmin@gmail.com)
 Phone Number Should Be 11 Char!
 Password Should Be 8 Char!
$---------------------------------------------------------------------------------------------------$
Something went wrong/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\Please Try Again After Somethime!
$---------------------------------------------------------------------------------------------------$
        """)
print("""
-------------------------------------------------------------------
                        ABC Register Panel
-------------------------------------------------------------------
""")
nam = str(input("Type Your Name: "))
ema = str(input("Type Your Email: "))
pho = str(input("Type Your Phone Number: "))
pas = getpass("Set Password: ")
con_pas = getpass("Set Confirm Password: ")
txt(nam,ema,pho,pas,con_pas)