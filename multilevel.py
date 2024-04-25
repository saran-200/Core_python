class college:
    def getStudentInfo(self):
        self.__rollno=input("enter the erollno")
        self.__name=input("enter the name")
    def printInfo(self):
        print("Rollnumber:",self.__rollno,"name:",self.__name)
class BE(college):
    def getBE(self):
        self.getStudentInfo()
        self.__p=int(input("entervthe physic mark"))
        self.__c=int(input("Enter the chem mark"))
        self.__m=int(input("ENter the maths mark"))
    def printBe(self):
        self.printInfo()
        print("MArks differnt",self.__p,self.__c,self.__m)
    def calculmarks(self):
        return (self.__p+self.__c+self.__m)
class Result(BE):
    def getResult(self):
        self.getBE()
        self.__total=self.calculmarks()
    def putResult(self):
        self.printBe()
        print("total mark 300",self.__total)
c=Result()
c.getResult()
c.putResult()
