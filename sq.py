num_of_numbers = int(input("Enter the number of numbers: "))
number_list = []
squared_list = []

i = 0
while i < num_of_numbers:
    i+=1
    num = int(input("Enter the number: "))
    number_list.append(num)

i=0
while i < num_of_numbers:
    num_squared = number_list[i] ** 2
    squared_list.append(num_squared)
    i += 1
print(squared_list[::-1])