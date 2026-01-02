import csv

"""
Book 클래스
"""
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed= False

"""
Member 클래스
"""
class Member:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.borrowed_book= []

    def add_book(self,book):
        self.borrowed_book.append(book)
    def show_book(self):
        for b in self.borrowed_book:
            print(f"{b.get("title")}")
    def remove_book(self,book):
        self.borrowed_book.remove(book)

"""
Library 클래스
"""
class Library:

    def __init__(self):
        self.library=[]
        self.library_members=[]

    def set_book(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader, start=1):
                my_book = Book(row["title"], row["author"], row["isbn"])
                self.library.append(my_book)

    def add_book(self,book):
        self.library.append(book)

    def show_library(self):
        for i,b in enumerate(self.library, start=1):
            print(f"{i}.이름 : {b.title} / 작가 : {b.author}  / isbn : {b.isbn}  / 도서의 대출상태 : {b.is_borrowed}")

    def set_member(self, member):
        self.library_members.append(member)

    def add_member(self,member):
        self.library_members.append(member)

    def show_member(self):
        for m in self.library_members:
            print(f"{m.name} / {m.phone}")

    def search_book(self,title):
        for b in self.library:
            if b.title == title:
                print(f"책이 존재 - {b.title} / {b.author} / {b.isbn} / {b.is_borrowed}")
                break
        else: print("도서관에 책이 없음")



