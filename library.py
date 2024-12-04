class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print("You borrowed")
        else:
            print("is not available.")

    def return_book(self):
        self.copies_available += 1
        print("You returned")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow_book()
                return
        print(" is not in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(" is not in the library.")

    def list_books(self):
        print("Library Books:")
        for book in self.books:
            print(f'"{book.title}" by {book.author} - {book.copies_available} copies')


book1 = Book("1984", "George Orwell", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 3)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 4)


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


library.borrow_book("1984")
library.borrow_book("The Great Gatsby")
library.return_book("1984")


library.list_books()
        
        
    
        
    
        
    