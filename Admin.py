from Book_info import user_book_register_code
from journals import user_journals_register_code


def Admin_functionality():
    """
        This function provides the admin functionality for the application.

        It allows users to add books or journals, or to logout.
        """

    print("  **** Welcome to admin page ****  ")

    while True:
        print("If you want to add Book then        press b"
              + "\nIf you want to add journal then     press j"
              + "\nLogout                              press O")
        choice = input("Enter your choice : ")

        if choice.lower()[0] == 'b':
            print("Add Book")
            user_book_register_code()
        elif choice.lower()[0] == 'j':
            print("Add journal")
            user_journals_register_code()
        elif choice.lower()[0] == 'o':
            exit(0)
        else:
            print("Invalid choice")
