class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author==self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
        



class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.book==self]
        return contracts

    def authors(self):
        return [contract.author for contract in self.contracts()]




class Contract:
    all = []

    def __init__(self, author, book, date):
        self.author = author
        self.book = book
        self.date = date
        Contract.all.append(self)

    @property
    def author(self):
        return self.a
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("value must be a instance of Author")
        self.a = value

    @property
    def book(self):
        return self.b
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("value must be a instance of Book")
        self.b = value

    @property
    def date(self):
        return self.d
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("vaule must be string")
        self.d = value



    


    
book = Book("Cool Book")
author1 = Author("Alice")
author2 = Author("Bob")

contract1 = Contract(author1, book, "2025-01-01")
contract2 = Contract(author2, book, "2025-02-01")

# list of objects
# print(book.contracts()) #[<__main__.Contract object at 0x102a8f850>, <__main__.Contract object at 0x102a8f890>]
# print(book.authors()) # [<__main__.Author object at 0x102a8d8d0>, <__main__.Author object at 0x102a8f810>]

print([author.name for author in book.authors()]) #['Alice', 'Bob']



