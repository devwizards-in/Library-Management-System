import pymongo


def Book_detail_for_user():
    """
        This function prints the details of all the books in the MongoDB collection.
    """

    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    books = Library.books  # collection name

    # Find all books in the collection
    book_detail = books.find()

    print("**************************************   Book Details  ****************************************")

    # Print the documents in the cursor
    for book in book_detail:
        # print(book)

        print("Title : " + book['title'] + "\t Author : " + book['author'] + "\t Genre :" + book[
            'genre'] + "\t publication year : " + book['publication_year'])

    print("***********************************************************************************************")


def Book_detail_search_according_to_requirement():
    """
        This function allows the user to search for books by title or author.
    """
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    books = Library.books  # collection name

    print("How do you want search ? " +
          "\naccording to Title :     press T " +
          "\naccording to Auther :    press A ")
    choice = input("Enter your Choice : ")

    if choice.lower()[0] == "t":
        # Get the value of the book title from the user
        title = input("Enter the book title: ")

        # Find the book in the collection
        book_detail = books.find({"title": title})

        print("**************************************   Book Details  ****************************************")

        # Print the documents
        for book in book_detail:
            # print(book)

            print("Title : " + book['title'] + "\t Author : " + book['author'] + "\t Genre :" + book[
                'genre'] + "\t publication year : " + book['publication_year'])

    elif choice.lower()[0] == "a":
        # Get the value of the book title from the user
        author = input("Enter the book Author : ")

        # Find the book in the collection
        book_detail = books.find({"author": author})

        print("book detail is", book_detail)
        print("**************************************   Book Details  ****************************************")

        # Print the documents
        for book in book_detail:
            # print(book)

            print("Title : " + book['title'] + "\t Author : " + book['author'] + "\t Genre :" + book[
                'genre'] + "\t publication year : " + book['publication_year'])

        print("***********************************************************************************************")


def book_availability(book_name):
    """
        This function checks if the book with the given name is available in the library.
    """
    print("book available or not")
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    books = Library.books  # collection name

    book_detail = books.find_one({"title": book_name})

    if book_detail is None:
        return "Book is not present"

    print("**************************************   Book Details  ****************************************")

    # Print the documents in the cursor
    for book in book_detail:
        # print(book)

        print("Title : " + book['title'] + "\t Author : " + book['author'] + "\t Genre :" + book[
            'genre'] + "\t publication year : " + book['publication_year'])
        return True



