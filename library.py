class library:
    def __init__(self,name,books):
        self.name=name
        self.book=books

    def display(self):
             print("BOOkS IN THE",self.name)
             print("#####################")
             for books in self.book:
                   print(books)
             print("#####################")

    def lend(self):
          global l
          l=input("Enter the book you want to lend: ").lower()
          le=self.book.remove(l)
          return le
    def add_book(self):
          add=input("Enter the book you want to add: ").lower()
          a=self.book.append(add)
          return a 
    def return_book(self):
          global l
          return_bk=input("Enter the book you want to return: ").lower()
          if l==return_bk:
                book_return=self.book.append(return_bk)
          else:
                print("Please return the correct book")

lib=library("Bangatan Library",["python","sql","power bi","html"])

while True:
     print("\t\t\t\t",lib.name)
     print("1.Display the books")
     print("2.Lend the book")
     print("3.Add a new book")
     print("4.Return a Book")
     print("5.Click q to quit")
     print()
     choice=int(input("Enter the choice from above: "))
     if choice==1:
        lib.display()
     elif choice==2:
        lib.lend()
     elif choice==3:
        lib.add_book()
     elif choice==4:
          lib.return_book()

     elif choice==5:
         quit()
    
        


        