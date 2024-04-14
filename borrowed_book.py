from connect_db import connect_db
from classes import Book

def borrowed_book(title):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "UPDATE Books SET availability = 0 WHERE title = %s"
            cursor.execute(query, (title,))
            conn.commit()
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_borrowed_book():
    while True:
        title = input("What book would you like to borrow?: ")
        borrowed_book(title)
        print(f"{title} has been checked out.")
        break