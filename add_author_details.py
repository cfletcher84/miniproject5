from connect_db import connect_db
from classes import Author

def author_details(name):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Authors WHERE name = %s"
            cursor.execute(query, (name,))
            author_info = cursor.fetchall()
            if author_info:
                print(author_info)
            else:
                print(f"Sorry, {name} does not exist in the Library.")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_author_details():
    while True:
        name = ((input("Enter the authors name to view their details: ")))
        author_details(name)
        break