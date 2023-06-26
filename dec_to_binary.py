dict = {
    1: 1,
    2: 10,
    3: 11,
    4: 100,
    5: 101,
    6: 110,
    7: 111,
    8: 1000,
    9: 1001,
    10: 1010
}

binary = ""
num = input("Enter a number: ")

for i in range(len(num)):
    letter = num[i]
    binary += str(dict[int(letter)])

print(binary)