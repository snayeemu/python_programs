def basic35(first_number, second_number):
    if first_number == second_number or abs(first_number - second_number) == 5 or first_number + second_number == 5:
        return True
    else:
        return False


if __name__ == "__main__":
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    output = basic35(first_number, second_number)
    print(output)
