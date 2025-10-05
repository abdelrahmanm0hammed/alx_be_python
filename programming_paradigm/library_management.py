class Book:
    def __init__(self, title, author):
        """Initialize a Book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track checkout status

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize an empty library collection."""
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """Add a Book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it’s available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Display all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")