class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.__class__.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
    
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author name: {self.name}>"


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.__class__.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"<Book title: {self.title}>"


class Contract:
    all_contracts = [] 

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        if royalties < 0:
            raise Exception("Royalties cannot be negative")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
    
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __repr__(self):
        return f"<Contract author: {self.author.name}, book: {self.book.title}, date: {self.date}, royalties: {self.royalties}>"

