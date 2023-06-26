num=int(input("enter a number"))
s=0
while(num!=0):
    rem=num%10
    
    s=(s*10)+rem
   
    num//=10
   
print("reverse=",s)