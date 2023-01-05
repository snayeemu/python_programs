def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    output = odd_or_even(number)
    print(f"Number is {output}")
