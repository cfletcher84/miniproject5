from connect_db import connect_db
from classes import Author

def add_author(name, biography):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            insert_info = (name, biography)
            query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, insert_info)
            conn.commit()
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_add_author():
    while True:
        action = input("Enter 'add' to add an author to your list: ").lower()
        if action == "add":
            name = input("\nWhat is the authors name?: ")
            biography = input("\nPlease enter the authors biography: ")
            new_author = Author(name, biography)
            add_author(new_author.name, new_author.biography)
            print(f"{new_author.name} has been added to the Library.")
            break
        else:
            print('Invalid input...please try again ┌( ಠ_ಠ)┘!')