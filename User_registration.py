# this code is for register user details

import pymongo

from user_login import user_login


def register_user(username, password, conform_password):
    """
        This function registers a new user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
            conform_password (str): The conform password of the user.

        Returns:
            The ObjectID of the newly created user.
    """

    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    users = Library.users  # collection name

    user = users.find_one({'username': username})
    if user is not None:
        print('Username already exists. Please use another username.')
        return False

    document = {
        'username': username,
        'password': password,
        'conform_password': conform_password,
        'borrow_book': [],
        'borrow_journal': []
    }

    result = users.insert_one(document)
    return result.inserted_id


# this is user registration code

def user_registration_code():
    username = input('Enter username : ')
    password = input('Enter password : ')
    conform_password = input('Enter conform password : ')

    if password == conform_password:
        id1 = register_user(username.lower(), password.lower(),
                            conform_password.lower())  # calling register user function
        if id1:
            print('User successfully registered with ObjectID: {}'.format(id1))
            user_login()
        else:
            print('user name is already exist')
            return user_registration_code()
    else:
        print("password and conform password is not same please enter both same !!! ")

    # user redirect on login
    print("Login page")
