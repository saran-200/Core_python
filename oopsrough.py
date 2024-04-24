class saran:
    def name(self):
        print("SARAN")
    def ac(self):
        print("987654321")
    def bal(self):
        print("23456")
    def ph(self):
        print("9344391267")
a=saran()
req=int(input("enter no of data required: "))
i=1
for i in range(i,(req+1)):
    ans=input("enter the tablename")
    if(ans=="name"):
        a.name()
    elif(ans=="ac"):
        a.ac()
    elif(ans=="bal"):
        a.bal()
    elif(ans=="ph"):
        a.ph()
    else:
        print("invalid input")
