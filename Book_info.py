import pymongo


def add_books(title, author, genre, publication_year):
    """
        This function adds a new book to the MongoDB collection.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
            publication_year (str): The publication year of the book.

        Returns:
            The ObjectID of the inserted book.
    """
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    books = Library.books  # collection name

    num_entries = books.count_documents({})

    book_id = "B10" + str(num_entries + 1)

    book = books.find_one({'title': title})
    if book is not None:
        print('Username already exists. Please use another username.')
        return False

    document = {
        'book_id': book_id,
        'title': title,
        'author': author,
        'genre': genre,
        "publication_year": publication_year
    }

    result = books.insert_one(document)
    return result.inserted_id


def user_book_register_code():
    """
    This function prompts the user to enter the details of a new book and then calls the `add_books()` function to
    add the book to the MongoDB collection.
    """
    title = input('Enter Title of Book : ')
    author = input('Enter Author of Book : ')
    genre = input('Enter Genre(like mystery,romance,sci-fi) of Book : ')
    publication_year = input('Enter publication year of Book : ')

    id1 = add_books(title.lower(), author.lower(), genre.lower(), publication_year.lower())  # calling register user function
    if id1:
        print('Book successfully registered with ObjectID: {}'.format(id1))
    else:
        print('Book name is already exist')
        return user_book_register_code()


# user_book_register_code()
