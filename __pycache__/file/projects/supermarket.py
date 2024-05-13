class market:
    def __init__(self,productid,productname,productquality,productprice,productrating,productbrand):
        self.__id=productid
        self.__name=productname
        self.__quality=productquality
        self.__price=productprice
        self.__rating=productrating
        self.__brand=productbrand
    def set_productid(self,productid):
        self.__id=productid
    def set_productname(self,productname):
        self.__name=productname
    def set_productquality(self,productquality):
        self.__quality=productquality
    def set_productprice(self,productprice):
        self.__price=productprice
    def set_productvaliddate(self,productrating):
        self.__rating=productrating
    def set_productpackages(self,productbrand):
        self.__brand=productbrand
    def get_productid(self):
        return self.__id
    def get_productname(self):
        return self.__name
    def get_productquality(self):
        return self.__quality
    def get_productprice(self):
        return self.__price
    def get_productrating(self):
        return self.__rating
    def get_productbrand(self):
        return self.__brand
    def __str__(self):
        return str(self.__id)+""+str(self.__name)+""+str(self.__quality)+""+str(self.__price)+""+str(self.__rating)+" "+(self.__brand)
prd=[]
rec=int(input("enter the requried no of records :"))
for i in range(rec):
    productid=int(input("product id :"))
    productname=input("product name: ")
    productquality=int(input("quality basedon star:"))
    productprice=int(input("product price "))
    productrating=int(input("rating"))
    productbrand=input("brand")       
    imp=market(productid,productname,productquality,productprice,productrating,productbrand)
    prd.append(imp)
for imp in prd:
    print( "the records are :::::::::")
    print("product id :",imp.get_productid())
    print("product name :",imp.get_productname())
    print("product quality :",imp.get_productquality())
    print("product price :", imp.get_productprice())
    print("product rating :",imp.get_productrating())
    print("product brand :",imp.get_productbrand())
#To search a product 
src=input("enter the product to search :")
for imp in prd:
    if(imp.get_productid()==src):
        print(imp)
        break
    else:
        print("data not found")
    