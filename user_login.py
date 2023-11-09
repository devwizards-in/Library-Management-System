# this code is for user login

import pymongo

from user_main import user_main_page


def login_user(username, password):
    """
        This function logs in the user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            True if the user was successfully logged in, False otherwise.
    """
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    users = Library.users  # collection name

    user = users.find_one({'username': username})
    if user is None:
        return False

    if password == user['password']:
        return True
    else:
        return False


def user_login():
    """
        This function prompts the user to enter their username and password and then logs them in if the credentials are valid.
    """
    while True:
        print("***************************** Welcome To Login Page **************************")
        username = input('Enter username: ')
        password = input('Enter password: ')

        user_name = username

        is_logged_in = login_user(username.lower(), password.lower())
        if is_logged_in:
            print("******************************************************************************")
            print('User successfully logged in.')
            print("******************************************************************************")
            user_main_page(user_name)  # this is main functionality of user

        else:
            print("******************************************************************************")
            print('Incorrect username or password.')
            print("******************************************************************************")
