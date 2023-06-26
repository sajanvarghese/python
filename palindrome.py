name=input("Enter the string ::")
leng=len(name)
temp=name
temp2=""
count=0
for i in range(1,leng+1):
    temp2+=name[leng-i]
    count+=1
print(temp2)
print("number of digits=",count)
if temp==temp2:
    print("string is palidrome")
else:
    print("not plaindrome")
