import pymongo


def Journal_detail_for_user():
    """
        This function prints the details of all the journals in the MongoDB collection.
    """
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    journals = Library.journals  # collection name

    # Find all books in the collection
    journal_detail = journals.find()

    print("**************************************   Book Details  ****************************************")

    # Print the documents in the cursor
    for journal in journal_detail:
        # print(book)

        print("Title : " + journal['title'] + "\t Author : " + "\t Field of Study :" + journal[
            'field_of_study'] + "\t publication year : " + journal['publication_year'])

    print("***********************************************************************************************")


def Journal_detail_search_according_to_requirement():
    """
        This function allows the user to search for journals by title or field of study.
    """
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    journals = Library.journals  # collection name

    print("******************************************************************************")
    print("How do you want search ? " +
          "\naccording to Title :     press T " +
          "\naccording to Field of study :    press F ")
    print("******************************************************************************")
    choice = input("Enter your Choice : ")

    if choice.lower()[0] == "t":
        # Get the value of the book title from the user
        title = input("Enter the Journal title : ")

        # Find the Journal in the collection
        journal_detail = journals.find({"title": title})

        print("**************************************   Journal Details  *************************************")

        # Print the documents
        for journal in journal_detail:
            print("Title : " + journal['title'] + "\t Author : " + "\t Field of Study :" + journal[
                'field_of_study'] + "\t publication year : " + journal['publication_year'])
            print("***********************************************************************************************")

    elif choice.lower()[0] == "f":
        # Get the field of study from the user
        field_of_study = input("Enter the Field of Study : ")

        # find the journal in the collection
        journal_detail = journals.find({"field_of_study": field_of_study})

        print("journal detail is", journal_detail)
        print("************************************** Journal Details ****************************************")

        # Print the documents in the cursor
        for journal in journal_detail:
            # print(book)

            print("Title : " + journal['title'] + "\t Author : " + "\t Field of Study :" + journal[
                'field_of_study'] + "\t publication year : " + journal['publication_year'])

        print("***********************************************************************************************")


def Journal_availability(journal_name):
    """
        This function checks if the journal with the given name is available in the library.

        Args:
            journal_name (str): The name of the journal.

        Returns:
            True if the journal is available, False otherwise.
    """
    print("book available or not")
    con = pymongo.MongoClient()  # making connection with mongodb
    Library = con['Library']  # database name
    journals = Library.journals  # collection name

    journal_detail = journals.find_one({"title": journal_name})

    if journal_detail is None:
        return "Book is not present"

    print("************************************  Journal Details  ****************************************")

    # Print the documents in the cursor
    for journal in journal_detail:
        # print(book)

        print("Title : " + journal['title'] + "\t Author : " + "\t Field of Study :" + journal[
            'field_of_study'] + "\t publication year : " + journal['publication_year'])
        return True


