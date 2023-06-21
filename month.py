dict={
    "january":31,
    "february":28,
    "march":31,
    "april":30,
    "may":31,
    "june":30,
    "july":30,
    "augest":31,
    "september":30,
    "october":31,
    "november":30,
    "December":31
}
list30=["april","june","July","september","november"]
list31=["january","march","August","october","December"]
list28=["February"]
day=input("what yoy want day/month ? :: ")
if day =="day":
 number=int(input("Enter the number of days"))
 if number==31:
    print(list31)
 elif number==30:
   print(list30)
 elif number==28:
   print(list28)
 else:
   print("invalid day")

elif day=="month":
   month=input("enter the month")
   mn=dict[month]
   print("Month ",mn)
else : 
    print("invalid input")