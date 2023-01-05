def sum_of_two_number(first_number, second_number):
    output = first_number + second_number
    if 15 <= output <= 20:
        return 20
    else:
       return output


if __name__ == "__main__":
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    output = sum_of_two_number(first_number, second_number)
    print(output)
