class BookDetails:
    """
    Надає детальну інформацію про книгу.
    """
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_book_info(self):
        """
        Повертає інформацію про книгу.
        """
        return f"{self.title} by {self.author}, published in {self.publication_year}"

class LibraryBook:
    def __init__(self, title, author, publication_year):
        self._book_details = BookDetails(title, author, publication_year)
        self.is_checked_out = False

    def check_out(self):
        """
        Видає книгу, якщо вона доступна.
        """
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Повертає книгу до бібліотеки.
        """
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def get_book_info(self):
        """
        Повертає інформацію про книгу.
        """
        return self._book_details.get_book_info()

# Використання коду
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book.check_out())
print(book.check_out())
print(book.get_book_info())