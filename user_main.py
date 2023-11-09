from Book_details_for_user import Book_detail_for_user
from Book_details_for_user import Book_detail_search_according_to_requirement
from Remove_borrow import Remove_journal, Remove_book
from borrow_book import borrow_book
from borrow_journal import borrow_journal
from journal_detail_for_user import Journal_detail_for_user, Journal_detail_search_according_to_requirement
from user_borrow import user_borrow, user_borrow_journal


def user_main_page(user_name):
    """
        This function is the main functionality of the user.

        Args:
            user_name (str): The username of the user.
    """

    print("******************************************************************************")
    print("                            Welcome in Library                                ")
    print("******************************************************************************")

    choice = input("You want Book or Journal  : ")
    print("******************************************************************************")

    if choice.lower()[0] == "j":
        while True:
            print("See all Journal :                                          press 1 " +
                  "\nSearch Journal  :                                          press 2 " +
                  "\nBorrow History :                                           press 3   " +
                  "\nBorrow Journal :                                           press 4" +
                  "\nReturn Borrow Journal :                                    press 5"
                  "\nExit :                                                     press 6")

            print("******************************************************************************")
            choice = int(input("Enter your choice : "))

            match choice:
                case 1:
                    Journal_detail_for_user()
                case 2:
                    Journal_detail_search_according_to_requirement()
                case 3:
                    user_borrow_journal(user_name)
                case 4:
                    borrow_journal(user_name)
                case 5:
                    Remove_journal(user_name)
                case 6:
                    exit(0)
                case _:
                    print("Pleas Enter correct number !!")
    elif choice.lower()[0] == "b":
        while True:
            print("See all book :                                             press 1 " +
                  "\nSearch book  :                                             press 2 " +
                  "\nBorrow History :                                           press 3" +
                  "\nBorrow Book :                                              press 4" +
                  "\nReturn Borrow Book:                                        press 5"
                  "\nExit :                                                     press 6")

            print("******************************************************************************")

            choice = int(input("Enter your choice : "))

            match choice:
                case 1:
                    Book_detail_for_user()
                case 2:
                    Book_detail_search_according_to_requirement()
                case 3:
                    user_borrow(user_name)
                case 4:
                    borrow_book(user_name)
                case 5:
                    Remove_book(user_name)
                case 6:
                    exit(0)
                case _:
                    print("Pleas Enter correct number !!")
    else:
        print("Pleas Enter Correct number")

# user_main_page()
