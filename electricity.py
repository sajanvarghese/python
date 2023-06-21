x=float(input("Enter the unit "))
if x<=100:
    print("No charge 0 RS")
elif x>100 and x <200:
    sub=x-100
    mul=sub*5
    print(mul,"RS")
elif x>=200:
    sub=x-100
    mul=sub*10
    print(mul,"RS")