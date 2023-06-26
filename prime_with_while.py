num=int(input("enter a number ::"))
flag=0
i=2
while(i<=(num/2)):
   if num%i==0:
        flag=1
   i+=1
if flag==0:
    print ("prime ")
else:
    print ("not prime")

    
        