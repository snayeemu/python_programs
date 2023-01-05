def euclideanGCD(number1, number2):
    while True:
        remainder = number1 % number2
        if remainder == 0:
            return number2
        else:
            number1 = number2
            number2 = remainder


print(euclideanGCD(6, 15))
