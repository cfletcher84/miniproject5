class Library:
    def main_menu():
        try:
            print("""
        Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit
                                
""")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
            


    def book_menu():
        try:
            print("""
        Welcome to the books section!
    
    Book Menu:
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books 
    6. Go Back
                  
""")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')       
   
            
    def user_menu():
        try:
            print("""
    Welcome to the user operations!
    
    User Operations:
    1. Add a new user
    2. View user details
    3. Display all users
    4. Go Back
              
""")   
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!') 
            
    def author_menu():
        try:
            print("""
              
    Welcome to the Authors section!
    
    Author Operations:
    1. Add a new author
    2. View author details
    3. Display all authors
    4. Go Back
              
""")
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')
