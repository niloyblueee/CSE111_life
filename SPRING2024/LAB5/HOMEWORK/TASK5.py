class Author:
    def __init__(self,name=''):
        self.name=name
        self.books={}
    def addBook(self,name,genre):
        if self.name!='':
            if  genre not in self.books.keys():  
                self.books[genre]=[]
                self.books[genre].append(name)
            else:
                self.books[genre].append(name)    
        else:
            print('A book can not be added without author name')
    def setName(self,name):
        self.name=name    
    def printDetail(self):
        print(f'Number of Book(s): {len(self.books.keys())}')
        print(f'Author Name: {self.name}')
        for i in self.books.keys():
            print(f"{i}: {', '.join(self.books[i])}")

a1 = Author() 
print("=================================") 
a1.addBook("Ice", "Science Fiction") 
print("=================================") 
a1.setName("Anna Kavan") 
a1.addBook("Ice", "Science Fiction") 
a1.printDetail() 
print("=================================") 
a2 = Author('Humayun Ahmed') 
a2.addBook("Onnobhubon", "Science Fiction") 
a2.addBook("Megher Upor Bari", "Horror") 
print("=================================") 
a2.printDetail() 
a2.addBook("Ireena", "Science Fiction") 
print("=================================") 
a2.printDetail() 
print("=================================")
