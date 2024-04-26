class account:
    def __init__(self,name="",num=0,bal=0):
        print("constructor called")
        self.__holder=name
        self.__accnum=num
        self.__accbal=bal
    def __add__(self,other):
        self.__accbal+=other
        print(other,"addded your current balanence is ",self.__accbal)
    def __sub__(self,other):
        if self. __accbal>=other:
            self.__accbal-=other
            print(others,"is debitted your current balance is ",self.__accbal)
        else:
            print(" insufficitent balance")
    def setholder(self,name=""):self.__holder=name
    def getholder(self):return self.__holder
    def setaccnum(self,num=0):self.__accnum=num
    def getaccnum(self):return self.__accnum
    def setaccbal(self,bal=0):self.__accbal=bal
    def getaccbal(self):return self.__accbal
a=account()
a.setaccbal(500)
a.setaccnum(12345)
a.setholder('saran')
print(a)
a+5000
print(a)
a+2345
print(a)



        
