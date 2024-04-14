from connect_db import connect_db
from classes import Book

def return_book(title):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "UPDATE Books SET availability = 1 WHERE title = %s"
            cursor.execute(query, (title,))
            conn.commit()
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_return_book():
    while True:
        title = input("Please enter the title of the book you would like to return: ")
        return_book(title)
        print(f"The book {title} has been returned.")
        break