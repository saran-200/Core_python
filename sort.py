lst=[]
i=1
for i in range (1,6):
    clr=input("enter the color")
    lst.append(clr)
print("before sorting",lst)
lst.sort()
print("after sorting",lst)