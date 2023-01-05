if __name__ == "__main__":
    given_string = input()
    numbers = []
    for element in given_string:
        if element.isnumeric():
            numbers.append(element)
    numbers.sort()
    output = ""
    i = 0
    for number in numbers:
        i += 1
        if i != (len(numbers)):
            output += str(number) + "+"
        else:
            output += str(number)
    print(output)
