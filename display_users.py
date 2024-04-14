from connect_db import connect_db
from classes import User

def display_users():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Users"
            cursor.execute(query)
            catalog = cursor.fetchall()
            print(f"Here are all the users in the Library: {catalog}")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()