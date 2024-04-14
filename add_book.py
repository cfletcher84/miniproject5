from connect_db import connect_db
from classes import Book
    
def add_book(title, author, genre, isbn, publication_date):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            insert_info = (title, author, genre, isbn, publication_date)
            query = "INSERT INTO Books (title, author, genre, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, insert_info)
            conn.commit()
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
        finally:
            cursor.close()
            conn.close()

def run_add_book():
    while True:
        action = input("Enter 'add' to add a book to the Library: ").lower()
        if action == "add":
            title = input("What is the title of the book you would like to add?: ")
            author = input(f"Who is the author for '{title}'?: ")
            genre = input(f"What is the genre of '{title}'? : ")
            isbn = int(input(f"What is the ISBN for '{title}'?: "))
            publication_date = input(f"What is the publication date for '{title}'? (yyyy/mm/dd): ")
            book = Book(title, author, genre, isbn, publication_date)
            add_book(book.title, book.author, book.genre, book.isbn, book.publication_date)
            print(f"{book.title} has been added to the Library.")
            break
        else:
            print('Invalid input...please try again ┌( ಠ_ಠ)┘!')