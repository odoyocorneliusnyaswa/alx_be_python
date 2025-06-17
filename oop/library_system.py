class Book:
    """Base class representing a book in the library system"""
    
    def __init__(self, title: str, author: str):
        """Initialize a book with title and author"""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of the book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book"""
    
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an ebook with title, author and file size
        Args:
            title (str): Title of the book
            author (str): Author of the book
            file_size (int): File size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation of the ebook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book"""
    
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a print book with title, author and page count
        Args:
            title (str): Title of the book
            author (str): Author of the book
            page_count (int): Number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation of the print book"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books"""
    
    def __init__(self):
        """Initialize an empty library"""
        self.books = []
    
    def add_book(self, book: Book):
        """
        Add a book to the library's collection
        Args:
            book (Book): Book instance to add (can be Book, EBook, or PrintBook)
        """
        if not isinstance(book, Book):
            raise ValueError("Can only add Book objects to the library")
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library"""
        if not self.books:
            print("The library has no books.")
            return
        
        print("Books in the library:")
        for book in self.books:
            print(f"- {book}")
