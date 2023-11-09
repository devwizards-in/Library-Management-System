import pymongo

from Book_details_for_user import book_availability


def borrow_book(user_name):
    """
        This function borrows a book from the library for the given user.

        Args:
            user_name (str): The username of the user.

        Returns:
            True if the book was borrowed successfully, False otherwise.
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
            user['borrow_book'].append(book_name)
            users.update_one({'username': user_name}, {'$set': {'borrow_book': user['borrow_book']}})
            print("    ******  Borrowed product  ******    ")
            return True



