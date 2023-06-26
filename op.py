def operation(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    else:
        return "Wrong input"

while True:
    choice = int(input("Continue or exit? (0/1): "))
    if choice == 0:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        op = input("Enter the operator (+ or -): ")

        result = operation(num1, num2, op)
        print("Result:", result)
    elif choice == 1:
      break
    else:
        print("Invalid choice. Please enter 0 or 1.")