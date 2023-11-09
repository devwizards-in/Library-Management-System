import pymongo


def Remove_journal(user_name):
    """
        This function removes a journal from the user's borrowed journals list.

        Args:
            user_name (str): The username of the user.

        Returns:
            True if the journal was successfully removed, False otherwise.
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
        print("This Journal is not present in library !!")
        print("******************************************************************************")
        return "Journal is not present"
    else:
        if borrow is None:
            return False

        for user in borrow:

            # remove element from array
            user['borrow_journal'].remove(journal_name)
            users.update_one({'username': user_name}, {'$set': {'borrow_journal': user['borrow_journal']}})
            print("    ******  Journal returned  ******    ")
            return True


def Remove_book(user_name):
    """
        This function removes a book from the user's borrowed books list.

        Args:
            user_name (str): The username of the user.

        Returns:
            True if the book was successfully removed, False otherwise.
    """
    con = pymongo.MongoClient()
    Library = con['Library']
    users = Library.users

    borrow = users.find({'username': user_name})

    book_name = input("Enter Book Name : ")

    # checking book is present or not
    books = Library.books  # collection name

    book_detail = books.find_one({"title": book_name})

    # book_availability(book_name)  # this function is use for check availability of book

    if book_detail is None:
        print("******************************************************************************")
        print("This book is not present in library !!")
        print("******************************************************************************")
        return "Book is not present"
    else:
        if borrow is None:
            return False

        for user in borrow:

            # remove element from array
            user['borrow_book'].remove(book_name)
            users.update_one({'username': user_name}, {'$set': {'borrow_book': user['borrow_book']}})
            print("    ******  Book returned  ******    ")
            return True


