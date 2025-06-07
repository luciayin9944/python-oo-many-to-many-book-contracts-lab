class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book==self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author==self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total




class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
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

    @property
    def royalties(self):
        return self.r
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be int")
        self.r = value

    @classmethod
    def contracts_by_date(cls, date):
        #return [contract for contract in Contract.all if contract.date == date]
        return [contract for contract in cls.all if contract.date == date]
    

    ##print contract list
    @classmethod
    def show_all(cls):
        for contract in cls.all:
            print(contract)
    
    def __repr__(self):
        return f"Contract(author={self.author.name}, book='{self.book.title}', date={self.date}, royalties={self.royalties})"
    




    
book1 = Book("Cool Book")
book2 = Book("Great Book")
author1 = Author("Alice")
author2 = Author("Bob")

contract1 = Contract(author1, book1, "2025-01-01", 100)
contract2 = Contract(author2, book1, "2025-02-01", 200)
contract3 = Contract(author2, book2, "2025-03-01", 300)

#print(Contract.all) #[<__main__.Contract object at 0x100601590>, <__main__.Contract object at 0x100602110>, <__main__.Contract object at 0x100602310>]
Contract.show_all()

# list of objects
# print(book.contracts()) #[<__main__.Contract object at 0x102a8f850>, <__main__.Contract object at 0x102a8f890>]
# print(book.authors()) # [<__main__.Author object at 0x102a8d8d0>, <__main__.Author object at 0x102a8f810>]

print([author.name for author in book1.authors()]) #['Alice', 'Bob']
print([author.name for author in book2.authors()])

print(author1.total_royalties())
print(author2.total_royalties())


