def lcm(first_number, second_number):
    i = 1
    while True:
        if i % first_number == 0 and i % second_number == 0:
            break
        i += 1
    return i


if __name__ == "__main__":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    lcm_number = lcm(first_number, second_number)
    print("Least common multiple is: ", lcm_number)
