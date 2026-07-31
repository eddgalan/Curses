from book import Book
from library import Library
from user import User

# Create Book
book1 = Book('El principioto', 'Antoine de Saint-Exupéry')
book2 = Book('1984', 'George Orwell')

# Create user
user1 = User('Juan', 'U0001')

# Create library
library1 = Library()

library1.add_book(book1)
library1.add_book(book2)

library1.add_user(user1)

# Show available books
library1.show_available_books()

# Borrow book
user1.borrow_book(book1)

library1.show_available_books() # Show available books

# Return book
user1.return_book(book1)

library1.show_available_books()

# ToDo: Hacer un ejercicio similar con una concesionaria de vehículos
