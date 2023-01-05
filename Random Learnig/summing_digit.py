if __name__ == "__main__":
    while True:
        sum_of_digit1 = []
        i = 0
        given_number1 = input()
        if int(given_number1) == 0:
            break
        while True:
            if i == 0:
                counter1 = 0
                for digit in given_number1:
                    counter1 += int(digit)
                i += 1
                sum_of_digit1.append(counter1)
            elif len(str(sum_of_digit1[-1])) > 1:
                counter1 = 0
                for digit in str(sum_of_digit1[-1]):
                    counter1 += int(digit)
                sum_of_digit1.append(counter1)
            else:
                print(sum_of_digit1[-1])
                break
