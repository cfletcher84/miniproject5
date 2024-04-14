import mysql.connector
from mysql.connector import Error

def connect_db():
    db_name = "library_management"
    user = "root"
    password = "Rice8941!"
    host = "localhost"

    try: 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host
        )

        return conn 


    except mysql.connector.Error as e:
        print(f'\nAn error {e} has occurred...please try again!')