maximum_number = int(input("Enter the maximum value: "))
for i in range(1, maximum_number + 1, 2):
    print(i, " ", end='' if i % 5 != 0 else "\n")