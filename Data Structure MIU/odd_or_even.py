def odd_or_even(given_number):
    return "odd" if given_number % 2 == 1 else "even"


if __name__ == "__main__":
    given_number = int(input("Enter a number: "))
    output = odd_or_even(given_number)
    print(f"The number is {output}")
