class book:
    def __init__(self,bookid,bookname,bookprice):
        self.__bookid=bookid
        self.__bookname=bookname
        self.__bookprice=bookprice
    def set_bookid(self,bookid):
        self.__bookid=bookid
    def set_bookname(self,bookname):
        self.__bookname=bookname
    def set_bookprice(self,bookprice):
        self.__bookprice=bookprice
    def get_bookid(self):
        return(self.__bookid)
    def get_bookname(self):
        return(self.__bookname)
    def get_bookprice(self):
        return(self.__bookprice)
    def __str__(self):
        return str(self.__bookid)+" "+self.__bookname+" "+str(self.__bookprice)
lib=[]
a=int(input("enter the items you required :"))
for i in range(a):
    bookid=int(input("enter the book id :"))
    bookname=input("enter the book name ")
    bookprice=int(input("enter the price of the amount :"))
    print("\n\n\n")
    books=book(bookid,bookname,bookprice)
    lib.append(books)

print(" view of the data ")
for book in lib:
    print("bookid:",book.get_bookid())
    print("bookname:",book.get_bookname())
    print("bookprice:",book.get_bookprice())

#search 
bookid=int(input("enter the required bookid :"))
for books in lib:
    if books.get_bookid()==bookid:
        print(books)
    else:
        print("invaild id ")
#delete 
bookid=int(input("enter the deleted bookid :"))
for books in lib:
    if books.get_bookid()==bookid:
        lib.remove(books)
        break
    print(books)
    