def difference_17(number):
    if number <= 17:
        return number - 17
    else:
        return abs((number - 17) * 2)


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    difference = difference_17(number)
    print(difference)
