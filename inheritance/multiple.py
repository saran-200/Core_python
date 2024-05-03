# multiple inheritance
class skillset:
    def __init__(self,name="",exp=0,poc=0):
        self.skill=name
        self.exp=exp
        self.poc=poc
    def view(self):
        return self.skill+" "+str(self.exp)+" "+str(self.poc)
class personal:
    def __init__(self,name,qual="",cnt=0,mail=""):
        self.name=name
        self.qualification=qual
        self.contact=cnt
        self.mailid=mail
    def __str__(self):
        return self.name+" "+self.qualification+" "+str(self.contact)+" "+self.mailid
class profile(personal,skillset):
    def __init__(self, name, qual="", cnt=0, mail="",s="",e=0,p=0):
        super(profile,self).__init__(name, qual, cnt, mail)
        self.skill=s;self.exp=0;self.poc=p
    def __str__(self):
        return super(profile,self).__str__()+" "+self.view()
pro=profile("sara","it",12345623,"saran@","python",5,2)
pro1=profile("karrth","it",1234567,"karth@","java",4,1)
print(pro)
print(pro1)


