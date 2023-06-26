num=int(input("Enter anumber"))
temp=num
ams=0
while(num>0):
    rem=num%10
    ams=ams+(rem*rem*rem)
    num//=10
if temp==ams:
    print("Amstrong")
else:
    print("Not amstrong")
