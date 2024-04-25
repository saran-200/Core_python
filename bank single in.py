class account:
    accno=0
    accbal=0
    accholder=""
    def __str__(self):
        return str(self.accno)+" "+self.accholder+" "+str(self.accbal)+"\n"
class card(account):
    cardnumber=0
    def __init__(self,cn=0,anum=0,ahold="",abal=0):
        self.cardnumber=cn
        self.accbal=abal
        self.accno=anum
        self.accholder=ahold
        self.transaction=[]
    def __add__(self,amt):
        self.accbal+=amt
        print(amt,"deposited to",self.accholder)
        self.transaction.append("credit")
    def __sub__(self,wdraw):
        if(self.accbal>=wdraw):
            self.accbal-=wdraw
            print(wdraw,"withdraw from ",self.accholder)
            self.transaction.append("debit")
        else:
            print("insufficitent account balance")
    def counttras(self):
        crecount=self.transaction.count("credit")
        debcount=self.transaction.count("debit")
        charges=0
        if(crecount>5):
            print(" ur extra amount for too much of credittion",(crecount-5)*10)
        elif(debcount>5):
            print(" ur extra amount for too much of debittion",(debcount-5)*10)
        def __str__(self):
            return str(super(card, self). __str__())+"\n"+str(self.cardnumber)+" "+str(self.accbal)+"\n"
a=account()
a.accno=456767;a.accholder="saran";a.accbal=1230
print(a)
c=card(1234567,456767,"saran",500.0)
c+358
print(c)
c+400
print(c)
c+100
print(c)
c+123
print(c)
c+10
print(c)
c+120
print(c)
c+100
print(c)
c.counttras()

       



       