from connect_db import connect_db
from classes import Book

def display_books():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Books"
            cursor.execute(query)
            catalog = cursor.fetchall()
            print(f"Here is a list of the books in the Library: {catalog}")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()