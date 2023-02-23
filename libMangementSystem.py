



class Library:
    # def __init__(self,list_of_books,libname):
    #     self.list_of_book = list_of_books
    #     self.libname = libname
    book_stock = {"Dark Psychology": "Arth",
                       "The Art of thinking": "Anaya",
                       "The power of Habit": "Parth",
                       "The Psychology of money": "Vikas",
                       "What if?": "Aric",
                       "Fairy Tale": "Gunjan",
                       "Rich dad, Poor dad": "Mahima",
                       "The Millionaire Next Door": "Harsh",
                       "Think like a Monk": "Payal",
                       "Bhagvat Geeta": "Heta"}
    lended_books = {}


    def display_book(self):
        for book,owner in self.book_stock.items():
            print (f"Book Name: {book}|| Last Owned by: {owner}")
    def lended_book(self):
        for book,owner in self.lended_books.items():
            print (f"Book Name: {book}|| Last Owned by: {owner}")

    def lend_book(self,username,bookname):
        if bookname in self.book_stock.keys():
            self.lended_books[bookname] = username
            del self.book_stock[bookname]
            print(f"Aprroved!")
        elif bookname in self.lended_books.keys():
            print(f"{bookname} is not avvailable RIght Now, {bookname} is taken by {self.lended_books[bookname]}")
        else:
            print("This Book Is not available")

    def add_book(self,username,bookname):
        self.book_stock[bookname]=username

    def return_book(self,username,bookname):
        if bookname in self.lended_books.keys():
            self.book_stock[bookname]=username
        else:
            print(f"{bookname} is not lended from here. if you want to donate books you can try add book option")


a = Library()
print("WELCOME TO THE A Library")
while True:
    option  = int(input("Enter Your choice: '1': Display all the avilable Books, '2': for Lend any Available Book, '3': Return a lended Book, '4': donate a book: "))
    if not isinstance(option,int):
        print("invalid key")
        continue


    if option == 1:
        a.display_book()
        continue
    elif option == 2:
        username = input("Please Enter your name: ")
        bookname = input("please Enter the book you want to borow: ")
        a.lend_book(username,bookname)
        continue
    elif option ==3:
        bookname = input("Please Enter Name of the Book you want to return: ")
        username = input("please Enter Your Name: ")
        a.return_book(username,bookname)
        continue
    elif option == 4:
        bookname = input("Please Enter Name of the Book you want to Donate: ")
        username = input("please Enter Your Name: ")
        a.add_book(username,bookname)
        continue
    else:
        pass

        continue

