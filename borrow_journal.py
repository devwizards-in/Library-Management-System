import pymongo


def borrow_journal(user_name):
    """
        This function borrows a journal from the library for the given user.

        Args:
            user_name (str): The username of the user.

        Returns:
            True if the journal was borrowed successfully, False otherwise.
    """
    con = pymongo.MongoClient()
    Library = con['Library']
    users = Library.users

    borrow = users.find({'username': user_name})

    journal_name = input("Enter Journal Name : ")

    # checking book is present or not
    journals = Library.journals  # collection name

    journal_detail = journals.find_one({"title": journal_name})

    # book_availability(book_name)  # this function is use for check availability of book

    if journal_detail is None:
        print("******************************************************************************")
        print("This book is not present in library !!")
        print("******************************************************************************")
        return "Book is not present"
    else:
        if borrow is None:
            return False

        for user in borrow:
            user['borrow_journal'].append(journal_name)
            users.update_one({'username': user_name}, {'$set': {'borrow_journal': user['borrow_journal']}})
            print("    ******  Borrowed product  ******    ")
            return True
