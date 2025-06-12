class Book:
    """Represents a book in the library system"""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available"""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out"""
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True
    
    def return_book(self):
        """Mark the book as returned/available"""
        if not self._is_checked_out:
            return False  # Wasn't checked out
        self._is_checked_out = False
        return True
    
    def is_available(self):
        """Check if the book is available for checkout"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a library containing a collection of books"""
    
    def __init__(self):
        """Initialize an empty library"""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a new book to the library's collection"""
        if not isinstance(book, Book):
            raise ValueError("Can only add Book objects to the library")
        self._books.append(book)
    
    def find_book(self, title):
        """Helper method to find a book by title (case-insensitive)"""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def check_out_book(self, title):
        """Check out a book by title if it's available"""
        book = self.find_book(title)
        if book is None:
            print(f"Book '{title}' not found in the library.")
            return False
        
        if book.check_out():
            print(f"Successfully checked out '{title}'")
            return True
        else:
            print(f"'{title}' is already checked out")
            return False
    
    def return_book(self, title):
        """Return a book by title if it was checked out"""
        book = self.find_book(title)
        if book is None:
            print(f"Book '{title}' not found in the library.")
            return False
        
        if book.return_book():
            print(f"Successfully returned '{title}'")
            return True
        else:
            print(f"'{title}' was not checked out")
            return False
    
    def list_available_books(self):
        """List all currently available books in the library"""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books currently available in the library")
            return
        
        print("Available books:")
        for book in available_books:
            print(f"  - {book}")
