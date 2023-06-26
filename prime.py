n = int(input("Enter a number: "))

print("Prime numbers up to", n, ":")

for num in range(2, n + 1):
    flag = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        print(num)