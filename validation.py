def passw_com(password_1, password_2):
    if len(password_1) == "":
        print("the password cannot be empty")
    elif password_1 != password_2:
        print("Wrong password")
    elif password_1 == password_2:
        print("correct password")
    elif len(password_1) < 8:
        print("the password must contain a minimum of 8 characters")
    else:
        print("")


def user_com(user_1, user_2):
        if len(user_1) == "":
            print("the user cannot be empty")
        elif user_1 == user_2:
            print("correct user")
        elif user_1 != user_2:
            print("Wrong user")
        else:
            print("")

def email_vali(f_user):
    if f_user.count('@') == 0:
        print("it is not an email")
    elif f_user.count('@') < 1:
        print("perfect")
    else:
        print("")





