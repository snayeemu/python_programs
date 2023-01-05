import math

if __name__ == "__main__":
    number_of_test_cases = int(input())
    for i in range(number_of_test_cases):
        number = int(input())
        result = 0
        j = 1
        while True:
            leading_zeroes = number // (5 ** j)
            if leading_zeroes > 0:
                result += leading_zeroes
                j += 1
            else:
                break
        print(result)
