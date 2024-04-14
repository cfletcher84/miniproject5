from connect_db import connect_db
from classes import User

def user_details(name):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Users WHERE name = %s"
            cursor.execute(query, (name,))
            user_info = cursor.fetchall()
            if user_info:
                print(user_info)
            else:
                print(f"Sorry, {name} does not exist in the Library.")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_user_details():
    while True:
        name = ((input("Enter the users name to view their details: ")))
        user_details(name)
        break