class mobile:
    __model=""
    __price=0
    __ram=0
    __internal=0
    def setmodel(self,mod=""):self.__model=mod
    def getmodel(self):return self.__model
    def setprice(self,pri=""):self.__price=pri
    def getprice(self):return self.__price
    def setram(self,ra=""):self.__ram=ra
    def getram(self):return self.__ram
    def setinternal(self,inter=""):self.__internal=inter
    def getinternal(self):return self.__internal
mob1=mobile()
mob1.setmodel("note11")
mob1.setinternal("64GB")
mob1.setprice("13k")
mob1.setram("4GB")
print(mob1.getinternal(),mob1.getmodel(),mob1.getprice(),mob1.getram())
