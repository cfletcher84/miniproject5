from connect_db import connect_db
from classes import User

def add_user(name, library_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            insert_info = (name, library_id)
            query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, insert_info)
            conn.commit()
        except Exception as e:
             print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_add_user():
    while True:
        action = input("Enter 'add' to add a user to your list: ").lower()
        if action == "add":        
            name = (input("Enter the user's name: "))
            library_id = int(input("Enter the user's library ID: "))
            user = User(name, library_id)
            add_user(user.name, user.get_library_id())
            print(f"{user.name} has been added to the Library Management System.")
            break
        else:
            print('Invalid input...please try again ┌( ಠ_ಠ)┘!')