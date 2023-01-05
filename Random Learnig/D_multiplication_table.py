if __name__ == "__main__":
    number_of_test_cases = int(input())
    for i in range(number_of_test_cases):
        step_counter = 0
        number = int(input())
        while number > 1:
            if number % 5 == 0:
                number = (number * 4) / 5
            elif number % 3 == 0:
                number = (number * 2) / 3
            elif number % 2 == 0:
                number /= 2
            else:
                step_counter = -1
                break
            step_counter += 1
        print(step_counter)

