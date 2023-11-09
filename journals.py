# This code is for journals registration into Database

import pymongo


def journals_books(title, field_of_study, publication_year):
    """
        This function registers a new journal into the MongoDB collection.

        Args:
            title (str): The title of the journal.
            field_of_study (str): The field of study of the journal.
            publication_year (str): The publication year of the journal.

        Returns:
            The ObjectID of the inserted journal.
    """
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    journals = Library.journals  # collection name

    num_entries = journals.count_documents({})
    journal_id = "J200" + str(num_entries + 1)

    journal = journals.find_one({'title': title})
    if journal is not None:
        print('Username already exists. Please use another username.')
        return False

    document = {
        'journal_id': journal_id,
        'title': title,
        'field_of_study': field_of_study,
        "publication_year": publication_year
    }

    result = journals.insert_one(document)
    return result.inserted_id


def user_journals_register_code():
    """
        This function prompts the user to enter the details of a new journal and then registers the journal into the MongoDB collection.
    """

    title = input('Enter Title of Journals : ')
    field_of_study = input('Enter Field of study (like mystery,romance,sci-fi) of Book : ')
    publication_year = input('Enter publication year of Book : ')

    id1 = journals_books(title.lower(), field_of_study.lower(), publication_year.lower())  # calling register user
    # function
    if id1:
        print('Book successfully registered with ObjectID: {}'.format(id1))
    else:
        print('Book name is already exist')
        return user_journals_register_code()



