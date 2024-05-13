print("::::::::::::::::: WELCOME TO BEDDYS PARK::::::::::::::::::::")
num=int(input("enter the total no of members :"))
cos=0
for i in range(num):
    per=int(input("enter the age :"))
    if(per>=10 and per<=18):
        a= 30
        print("your in teenerzone :")
        cos=a
        print("your cost for the teeners",cos)

    elif(per<=50 and per>=19):
        a=60
        print("your in adultzone :")
        cos=a
        print("your cost for the teeners",cos)
    elif(per>=50 and per<=80):
        a=50
        print("your in olderzone")
        cos=a
        print("your cost for the teeners",cos)
    else:
        print("invaild input")
# tot=cos+cos
print(tot)