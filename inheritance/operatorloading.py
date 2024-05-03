# class opera:
#     def __init__(self,a):
#         self.a=a
#         print(self.a+self.a)

# o=opera(10)
# o1=opera(20)
# print("sum :",o1.a+o.a)


class opera:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
o=opera(50)
o1=opera(100)
print("sum",o+o1)