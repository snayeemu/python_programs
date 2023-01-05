def basic33(three_given_numbers):
    output = 0
    if three_given_numbers[0] != three_given_numbers[1] and three_given_numbers[0] != three_given_numbers[2] and \
            three_given_numbers[1] != three_given_numbers[2]:
        for element in three_given_numbers:
            output += element
    return output


if __name__ == "__main__":
    three_given_numbers = list(map(int, input("Enter three numbers: ").strip().split(" ")))[:3]
    output = basic33(three_given_numbers)
    print(output)
