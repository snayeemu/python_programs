def find_maximum(given_numbers):
    maximum_number = given_numbers[0]
    for element in given_numbers:
        if maximum_number < element:
            maximum_number = element
    return maximum_number


if __name__ == "__main__":
    given_numbers = list(map(int, input("Enter three numbers: ").split(" ")))
    maximum_number = find_maximum(given_numbers)
    print(f"Maximum number is {maximum_number}\n", "maximum number is greater than 100" if maximum_number > 100 else "")
