print('.......................................WELCOME TO CHILL THEAM PARK .....................................')
# n=int(input("enter the total number of members :"))
age=int(input('enter your age :'))
# for i in range(n):
    if( age>=10 and age<=60):
        if(age>=10 and age<=18):
            print(" you are eligible for kids zone")
            count1=int(input('enter the count of kids'))
            amt1=count1*600
            cam=input(' If you need to access camera type "YES" or " NO"  NOTE: extra charges ')
            if(cam=="yes"):
                chr=200
                print('charges for camera ',chr)
            else:
                chr=0
            total=amt1+chr
            print('amount for kids',total)
            print('kindly move to the kids zone in the left ')
            print('HAPPY JOURNEY')
        elif(age<=35 and age>=18):
            print('you are eligible for adults zone')
            count2=int(input('enter the count of adults'))
            amt2=count2*800
            cam=input(' If you need to access camera type "YES" or " NO"  NOTE: extra charges ')
            if(cam=="yes"):
                chr=200
                print('charges for camera ',chr)
            else:
                chr=0
            total1=amt2+chr
            print('amount for adluts',total1)
            print('kindly move to the adults zone in the right ')
            print('HAPPY JOURNEY')
        elif(age<=60 and age>=36):
            print('semi aged')
            count3=int(input('enter the count of semi aged persons'))
            amt3=count3*650
            cam=input(' If you need to access camera type "YES" or " NO"  NOTE: extra charges ')
            if(cam=="yes"):
                chr=200
                print('charges for camera ',chr)
            else:
                chr=0
            total2=amt3+chr
            print('amount for kids',amt3+chr)
            print('kindly move to the semiaged zone in the straight ')
            print('HAPPY JOURNEY')
        #print('TOTAL =',total+total1+total2)
    else:
        print('your not eligible')
