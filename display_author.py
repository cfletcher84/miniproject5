from connect_db import connect_db
from classes import Author

def display_authors():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Authors"
            cursor.execute(query)
            catalog = cursor.fetchall()
            print(f"\nHere are the authors in the Library: {catalog}")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()