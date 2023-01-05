def basic38(first_number, second_number):
    return (first_number + second_number) ** 2


if __name__ == "__main__":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    output = basic38(first_number, second_number)
    print(f"({first_number} + {second_number}) ^ {2} = {output}")
