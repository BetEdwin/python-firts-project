def print_welcome_message():
    print("---------------access validator with username and password------------")
import validation
print_welcome_message()
user="riabeta@gmail.com"
password="Briano97"

user_v= input(str("enter user"))
password_v= input(str("enter password"))

if (user == user_v) and (password==password_v):
    validation.passw_com(user,user_v)
    validation.user_com(password, password_v)
    print("LOGIN PERFECT")

elif( user != user) or (password != password_v):
    validation.email_vali(user_v)
    validation.passw_com(user,user_v)
    validation.user_com(password, password_v)
    print("ERROR")
else:
    print("")




