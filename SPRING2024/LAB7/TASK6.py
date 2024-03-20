class  Library:
    def __init__(self,name,bookDet):
        self.name=name
        self.books=bookDet
        self.borrower={}
    def details(self):
        print(f'{self.name} library details\nBorrower details:\n{self.borrower}\nBooks available:\n{self.books}')


class Reader:
    def __init__(self,name):
        self.name=name
        self.books=0
        self.details={}
    def borrow(self,library,*books):
        for i in books:
            if self.books!=5 :
                if library.books[i]!=0:
                    self.books+=1
                    library.books[i]-=1
                    print(f'{i} book is borowed succesfully')
                    library.borrower[self.name]=self.books
                    if i in self.details.keys():
                        self.details[i]+=1
                    else:
                        self.details[i]=1
                else:
                    print(f'{i} books are not available at the moment.')                        
            else:
                print('You cannot borrow more than 5 books.')
    def readerInfo(self,book=''):
        if book == '':
            print(f'{self.name}, you have {self.books} book(s) woth you.')
            for i in self.details.keys():
                print(f'Books on {i}: {self.details[i]}')
        else: 
            print(f'{self.name}, you have {self.details[book]} {book} books(s)with you')     

L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()
