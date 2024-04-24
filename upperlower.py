Str=input('enter the paragraph')
def par(str):
    lower=0
    upper=0
    indent=0
    for i in Str:
        if(i.islower()):
                lower+=1              
        elif(i.isupper()):
                upper+=1  
        else:
             indent+=1      
    print("The total no of letters is :",(lower+upper+indent))
    print("The number of lowercase characters is:",lower)
    print("The number of uppercase characters is:",upper)
    print("The number of indent characters is:",indent)
par(str)
