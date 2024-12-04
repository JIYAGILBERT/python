# class Book:
#     def __init__(self, title, author, copies_available):
#         self.title = title
#         self.author = author
#         self.copies_available = copies_available

#     def borrow_book(self):
#         if self.copies_available > 0:
#             self.copies_available -= 1
#             print(f'You borrowed "{self.title}".')
#         else:
#             print(f'"{self.title}" is not available.')

#     def return_book(self):
#         self.copies_available += 1
#         print(f'You returned "{self.title}".')

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def borrow_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 book.borrow_book()
#                 return
#         print(f'"{title}" is not in the library.')

#     def return_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 book.return_book()
#                 return
#         print(f'"{title}" is not in the library.')

#     def list_books(self):
#         print("Library Books:")
#         for book in self.books:
#             print(f'"{book.title}" by {book.author} - {book.copies_available} copies')

# # Create books
# book1 = Book("1984", "George Orwell", 5)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 3)
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 4)

# # Create library and add books
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # Borrow and return books
# library.borrow_book("1984")
# library.borrow_book("The Great Gatsby")
# library.return_book("1984")

# # List books with current availability
# library.list_books()


class Book:
    def __init__(self, title, copies): 
        self.title = title
        self.copies = copies
        
    def borrow(self): 
        self.copies -= 1 if self.copies > 0 else print(f'{self.title} not available')
    def return_book(self): self.copies += 1

class Library:
    def __init__(self): self.books = []
    def add(self, book): self.books.append(book)
    def search(self, title): return next((b for b in self.books if b.title == title), None)
    def list_books(self): [print(f'{b.title}: {b.copies} copies') for b in self.books]

# Create books and library
library = Library()
book1, book2, book3 = Book("1984", 5), Book("Mockingbird", 3), Book("Gatsby", 4)
library.add(book1), library.add(book2), library.add(book3)

# Borrow, return and list books
book1.borrow(), book3.borrow(), book1.return_book()
library.list_books()
