if __name__ == "__main__":
    number_of_test_cases = int(input())
    for i in range(number_of_test_cases):
        counter = 0
        given_string = input()
        for element in given_string:
            if element == '.':
                counter += 1
                try:
                    float(given_string)
                    print(True)
                    break
                except ValueError:
                    print(False)
                    break
        if counter == 0:
            print(False)
