from connect_db import connect_db
from menu import Library
import add_book, borrowed_book, return_book, search_book, display_books
import add_user, display_users, user_details
import add_author, add_author_details, display_author

def library():
    while True:
        try:
            Library.main_menu()
            user_input = input("\nWhich option would you like to choose? 1-4: ")
            if user_input == '1':
                book_menu()
            elif user_input == '2':
                user_menu()
            elif user_input == '3':
                author_menu()
            elif user_input == '4':
                return
            else:
                print('Invalid input...please try again ┌( ಠ_ಠ)┘!')
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')

def book_menu():
    while True:
        try:
            Library.book_menu()
            user_input = input('\nWhat would you like to do today?: ')
            if user_input == '1':
                add_book.run_add_book()
            elif user_input == '2':
                borrowed_book.run_borrowed_book()
            elif user_input == '3':
                return_book.run_return_book()
            elif user_input == '4':
                search_book.run_search_book()
            elif user_input == '5':
                display_books.display_books()
            elif user_input == '6':
                return
            else:
                print('Invalid input...please try again ┌( ಠ_ಠ)┘!')
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')

def user_menu():
    while True:
        try:
            Library.user_menu()
            user_input = input('\nPlease choose an option (1-4): ')
            if user_input == '1':
                add_user.run_add_user()
            elif user_input == '2':
                user_details.run_user_details()
            elif user_input == '3':
                display_users.display_users()
            elif user_input == '4':
                return
            else:
                print('Invalid input...please try again ┌( ಠ_ಠ)┘!')  
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')

def author_menu():
    while True:
        try:
            Library.author_menu()
            user_input = input('\nPlease choose an option (1-4): ')
            if user_input == '1':
                add_author.run_add_author()
            elif user_input == '2':
                add_author_details.run_author_details()
            elif user_input == '3':
                display_author.display_authors()
            elif user_input == '4':
                return
            else:
                print('Invalid input...please try again ┌( ಠ_ಠ)┘!')  
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')

library()           