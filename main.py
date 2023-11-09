"""
This code is writen by devwizards.in
"""

# This is the mail file of this project wich control all project
from Admin import Admin_functionality
from User_registration import register_user, user_registration_code
from user_login import user_login

if __name__ == '__main__':
    print("Welcome in code !!")

    print("Login as user :          press U ")
    print("Login as admin :         press A ")

    choice = input("Enter Your choice : ")
    if choice.lower()[0] == "u":
        print("******************************************************************************")
        print("Login or register : " +
              "\nif you want login press : L " +
              "\nif you want to Register the press : R"
              )
        print("******************************************************************************")

        user_choice = input("Enter your choice : ")
        u_c = user_choice.lower()[0]

        print(u_c)

        if u_c == 'l':
            user_login()

        elif u_c == 'r':
            print("you are in registration")
            user_registration_code()  # this function use for registration of user
        else:
            print("Please enter valid information !!!")

    elif choice.lower()[0] == "a":
        Admin_functionality()

