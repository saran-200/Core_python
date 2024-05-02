from pickle import *
data=open("beddy.txt","wb")
a=[1234,1234,2345,45,34,34]
b=[2367,6762,45642,75632]
c={"sasdf","wrer","etryt"}
dump(a,data)
dump(b,data)
dump(c,data)
data.close()
