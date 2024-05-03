print('...................................WELCOME TO AIYO ATM...................................')
print('.........................insert your card.............')
passwd=int(input(' enter the PIN number :'))
if(passwd==1234):
    userinp=input("deposite or withdraw or balance enquiry :")
    balance=10000
    if(userinp=="deposite"):
        dep_amt=int(input('enter the amount of deposite:'))
        print("ur deposite amt is",dep_amt,"ur current balance is ",(balance+dep_amt))
    elif(userinp=="withdraw"):
        wd_amt=int(input('enter the amount of withdraw :'))
        print('ur withdraw amount is',wd_amt,'ur current balance is',(balance-wd_amt))
    elif(userinp=="balance enquiry"):
        print('your balance is ',balance)
    else:
        print('transaction declined')
else:
    print("incorrect passwrd")

