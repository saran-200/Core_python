da=open("./beddy.txt",'w') # to create the new file or old file
da.write("hello everyone")# to  write in the file
print(da.name)# to print the file name 
print(da.mode)#to print the mode of the function 
print(da.readable())# to check if it is readable mode 
print(da.writable())# to check if it is in write mode  

da.close()