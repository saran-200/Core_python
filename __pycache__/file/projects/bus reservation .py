print('.........................WELCOME TO BKS TRANSPORT...................')
seats=0
av_seats=int(input('enter the available seats:'))
while (seats<=av_seats):
    a=int(input('enter the no of seats required'))
    if(av_seats >=a):
        amt=a*400
        print('your tickets price is ',amt)
        if(a>1):
            print('your booked seat number is from ',seats,"to",(seats + (a-1)))
        else:
            print('your seat number is',seats)
        seats+=a
        av_seats-=seats
        print('booked seats',seats)
        print('availabe seats',av_seats)
    else:
        print('insufficient seat')   
    

