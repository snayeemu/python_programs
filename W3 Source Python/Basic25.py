list1 = [1, 5, 8, 3]
input_value = int(input("Enter value for search: "))
try:
    output = list1.index(input_value)
    print("True")
except ValueError:
    print("False")
