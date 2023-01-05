def gcd(first_number, second_number):
    loop_controler = 0
    if first_number > second_number:
        loop_controler = first_number
    else:
        loop_controler = second_number
    for i in range(loop_controler, 1, -1):
        if first_number % i == 0 and second_number % i == 0:
            return i


if __name__ == "__main__":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    output = gcd(first_number, second_number)
    print(f"The greatest common divisor {output}")
