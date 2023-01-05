number = int(input("Enter a number: "))
numbers = []
for i in range(1, 4):
    numbers.append(str(number) * i)
result = 0
for i in range(len(numbers)):
    result += int(numbers[i])
print(f"Result {result}")