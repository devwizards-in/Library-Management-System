# this code is for display borrow items by user

import pymongo


def user_borrow(user_name):
    """
        This function displays the borrowed items of the user.

        Args:
            user_name (str): The username of the user.
    """
    print("this is user borrow function")
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    users = Library.users  # collection name

    borrow = users.find({'username': user_name})

    if borrow is None:
        return False

    for user in borrow:
        if user['borrow_book']:
            print("******************************************************************************")
            print("The borrow items are:")
            for item in user['borrow_book']:
                print(item)

            print("******************************************************************************")
        else:
            print("******************************************************************************")
            print("You have not borrowed any books.")
            print("******************************************************************************")


# this function is for borrow junrnals
def user_borrow_journal(user_name):
    """
        This function displays the borrowed journals of the user.

        Args:
            user_name (str): The username of the user.
    """

    # print("this is user borrow function")
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    users = Library.users  # collection name

    borrow = users.find({'username': user_name})

    if borrow is None:
        return False

    for user in borrow:
        if user['borrow_journal']:
            print("******************************************************************************")
            print("The borrow items are:")
            for item in user['borrow_journal']:
                print(item)

            print("******************************************************************************")
        else:
            print("******************************************************************************")
            print("You have not borrowed any journal.")
            print("******************************************************************************")
