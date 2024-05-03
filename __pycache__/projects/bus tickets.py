print('............................................Welcome To KANTHAN Transport ...................')
s='salem'
am='ammapet'
a=' A.patanam'
v='valappati'
p='P.N.palayam'
at='attur'
stage_1=input("enter stage 1:" )
stage_2=input("enter stage 2 :")
if(stage_1=='s' and stage_2=='at'):
    print(s,'to',at,'RS = 35')
elif((stage_1=='s'and stage_2=='am')or(stage_1=='am'and stage_2=='a') or(stage_1== 'a' and stage_2== 'v')or(stage_1=='v'and stage_2=='p')or(stage_1=='p' and stage_2=='at')):
    print('RS= 10')
elif((stage_1=='s' and stage_2=='a') or (stage_1=='am' and stage_2=='v')or(stage_1=='a'and stage_2=='p') or(stage_1=='v'and stage_2=='at')):
   print('RS= 15')
elif((stage_1=='s' and stage_2=='v') or(stage_1=='am'and stage_2=='p')or(stage_1=='a'and stage_2=='at')):
    print('RS= 20')
elif((stage_1=='s' and stage_2=='p')or(stage_1=='am'and stage_2=='at')):
    print('RS= 25')
else:
    print('invaild input')

    

    