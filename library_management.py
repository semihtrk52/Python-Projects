class Book:
    def __init__(self, title, author, isbn, publication_year, page_number) -> None:
        self.title = title #str
        self.author = author #str
        self.publication_year = publication_year #int
        self.isbn = isbn #str
        self.page_number = page_number #int
        self.is_borrowed = False  #bool true or false

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class Member:
    def __init__(self,member_id, name) -> None:
        self.name = name #str
        self.member_id = member_id
        self.borrowed_books = [] # list

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False


class Library:
    def __init__(self) -> None:
        self.books = [] #list
        self.members = [] #list

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn and not b.is_borrowed), None)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn and b.is_borrowed), None)
        if member and book:
            return member.return_book(book)
        return False

    def list_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def list_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed]

library = Library()

# Kitap ekleme
book1 = Book("Gece Yarısı Kütüphanesi", "Matt Haig", "1234567890", 2021, 296)
library.add_book(book1)

# Üye ekleme
member1 = Member("M001", "Alice")
library.add_member(member1)

book2 = Book("Kürk Mantolu Madonna", "Sabahattin Ali", "123456788", 2001, 156)
library.add_book(book2)

# Kitap ödünç alma
library.borrow_book("M001", "1234567890")

# Mevcut kitapları listeleme
available_books = library.list_available_books()
borrowed_books = library.list_borrowed_books()

print("Mevcut Kitaplar:", [book.title for book in available_books])
print("Ödünç Alınan Kitaplar:", [book.title for book in borrowed_books])