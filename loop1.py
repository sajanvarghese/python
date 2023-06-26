x=int(input("enter the limit"))
x>1
for num in range(0,x+1):
 for i in range(2,int(num**0.5)+1):
    if(i%x)==0:
        print(x)

