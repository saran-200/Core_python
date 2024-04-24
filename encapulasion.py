# class bank:
#     value=190
#     def saran(self):
#         print("name : saran")
#         print("accno : 879605432")
#         print("place : valapadi\n")

#     def karthi(self):
#         print("name : karthi")
#         print("accno : 8723456723")
#         print("place : P.N.palayam")
# a=bank()
# a.saran()
# a.karthi()

# ======> to keep the function as private
class bank:
    def __init__(self):
        self.__values=12
    def __sara(self):
        print("name : saran")
        print("accno : 879605432")
        print("place : valapadi")
        print("values",self.__values,"\n")
    def __kar(self):
        print("name : karthi")
        print("name : karthi")
        print("accno : 8723456723")
        print("place : P.N.palayam")
b=bank()
b._bank__sara()
b._bank__kar()