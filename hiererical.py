#hierarchy inhertitance
from array import *
class stock:
    product=array("i")
    def show(self):
        print("product :",self.product)
    def search(self):
        budget=int(input("enter your budget"))
        for x in self.product:
            if x<=budget:
                print(x)
class smart(stock):
    def __init__(self,hey):
        self.product=array('i')
        self.product.extend(hey)   
class DMART(stock):
    def __init__(self,hai) :
        self.product=array('i')
        self.product.extend(hai)
    def getbyposition(self,start,stop):
        print(self.product[start:stop])
s=smart([12,100,150,250,200])
s1=DMART([100,200,300,800])
s1.getbyposition(0,4)
s1.show()
s.show()
s1.search()
