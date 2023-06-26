dict= {
    0:"Zero",
    1: "One",
    2: "two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}
integer=int(input("Enter a number"))
output = [int(x) for x in str(integer)]
print(output)
for i in range(len(output)):
    ls=output[i]
    print(dict[int(ls)])
