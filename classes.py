class Book():

    def __init__(self, title, author, isbn, genre, publication_date):
        try:
            self.title = title
            self.author = author
            self.isbn = isbn
            self.genre = genre
            self.publication_date = publication_date
            self.is_available = True
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')

class User:
    def __init__(self, name, library_id):
        try:
            self.name = name
            self.__library_id = library_id
            self.borrowed_books = []
        except Exception as e:
            print(f'\nAn error {e} has occurred...please try again ┌( ಠ_ಠ)┘!')

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, new_library_id):
        self.__library_id = (new_library_id)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        return self.name

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def get_name(self):
        return self.name
    
    def get_biography(self):
        return self.biography