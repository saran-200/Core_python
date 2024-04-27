# try:
#     a=10
#     b=0
#     c=a/b
#     print(c)
# except Exception as o:
#     print("zerodivision error",o)

# try:
#     class a:
#         def name(self):
#             print("name")
#         pass
#     s=a()
#     s.name()
# except Exception as p:
#     print(p)
#     print("errror")

#=====> values error <====================

# try:
#     mon=int(input("enter your month salary: "))
#     print("your annual salary ",mon*12)
# except Exception as e:
#     print("values error ")
#     mon1=int(input("enter your salary :"))
#     print("your annual salary is :",mon1*12)


# index error handliing 
# lst=[12,23,345,45,"sr"]
# tup=(9,87,"beddy",00)
# from array import *
# arr=array('b',[1,2,3,4])
# s="sarab"
# try:
#     it=int(input("index pls"))
#     print(lst[it],tup[it],arr[it],s[it])
# except Exception as e :
#     print(e)
#     ind=int(input("index pls: "))
# finally:
#     print("thank you welcome again")