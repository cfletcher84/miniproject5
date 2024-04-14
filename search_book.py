from connect_db import connect_db
from classes import Book

def search_book(title):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Books WHERE title = %s"
            cursor.execute(query, (title,))
            book_title = cursor.fetchall()
            if book_title:
                print(book_title)
            else:
                print(f"Sorry, {title} does not exist in the Library.")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_search_book():
    while True:
        title = input("Please enter the title of the book you are searching for: ")
        search_book(title)
        break