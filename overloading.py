# overloading (same function name and different parameters)

# class sam:
#     def aaa(self,a):
#         print(a)
#     def aaa(self,a,b):
#         print(a+b)
#     def aaa(self,a,b,c):
#         print(a+b+c)
# s=sam()
# s.aaa(12,23,34)


# class over:
#     def load(self,a=0,b=0,c=0):
#         if a!=0 and b!=0 and c!=0:
#             print(a+b+c)
#         elif a!=0 and b!=0:
#             print(a+b)
#         else:
#             return a
# o=over()
# print("sum",o.load(10))
# print("sum",o.load(10,20,30))
# print("sum",o.load(10,50))

# class multiple:
#     def add(self,*args):
#         sum=40
#         for i in args:
#             sum+=i
#         print("add values :",sum)
# a=multiple()
# a.add(2,23,34,23,2,2,32,2,3,23)
