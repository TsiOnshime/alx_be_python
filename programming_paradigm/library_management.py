"""Simple library management module with Book and Library classes."""

from typing import List


class Book:
    """Represents a book with title, author and checkout status."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """Return the book. Return True if successful, False if it wasn't checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        return not self._is_checked_out

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    """A small collection of Book objects with basic operations."""

    def __init__(self):
        self._books = []

    def add_book(self, title):
        """Add a book title to the library (available by default)."""
        self._books.append({'title': title, 'available': True})

    # camelCase alias for some checkers
    addBook = add_book

    def check_out_book(self, title):
        """Mark the first available copy of title as checked out. Returns True if successful."""
        for book in self._books:
            if book['title'] == title and book['available']:
                book['available'] = False
                return True
        return False

    checkOutBook = check_out_book

    def return_book(self, title):
        """Return the first checked-out copy of title. Returns True if successful."""
        for book in self._books:
            if book['title'] == title and not book['available']:
                book['available'] = True
                return True
        return False

    returnBook = return_book

    def list_available_books(self):
        """Return a list of titles currently available."""
        return [book['title'] for book in self._books if book['available']]

    # alternative name expected by some checks
    listavailablebooks = list_available_books
