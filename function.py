# def add(a,b):
#     print(a+b)
# add(12,23)
# def sub(a,b):
#     print(a-b)
# sub(1,3)


# def grt():
#     a=int(input('enter the number :'))
#     if(a<=8): print('hello')
#     elif(a>=0): print('hai')
#     else: print('bye')
# grt()

# def interview (degree,exper):
#     if(degree=="BE" and exper==5):
#         print("your eligible for 70k")
#     elif( degree=="ME" and exper==4):
#         print("your eligible for 75k ")
#     elif(degree=="bsc" and exper==5):
#         print("your eligible for 35k")
#     else:
#         print(" your fired")
# degree=input("enter your degree :")
# # exper=int(input('enter your experience :'))
# # interview(degree,exper)
# def register(name,location,prefix="mr/mrs/miss"):
#     if(location=="salem"):
#         print(name,location,prefix)
#     elif(name=='saran'):
#         print(prefix,name,"from",location)
#     else:
#         print('invaild input')
# name=input('enter the values')
# location=input("enter the location")
# prefix=input(" your sulitation")
# register(name,location,prefix)

bal=[10000,20000,30000,4560]
def debit( money,pos):
    if(money<=bal[pos]):
        print(money,"is debited")
        b=bal[pos]-money
        return(b)
    else:
        print('insufficent balance')
pos=int(input('enter the acc no '))
money=int(input( 'money to debit'))
debit(money,pos)

