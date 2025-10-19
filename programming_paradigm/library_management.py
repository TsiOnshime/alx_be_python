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
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def check_out_book(self, title: str) -> bool:
        """Check out the first available book matching title. Returns True on success."""
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title: str) -> bool:
        """Return the first checked-out book that matches the title. Returns True on success."""
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self) -> None:
        """Print available books, one per line. If none, print a message."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No available books.")
            return
        for book in available:
            print(book)
