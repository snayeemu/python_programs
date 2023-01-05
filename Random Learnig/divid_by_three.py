if __name__ == "__main__":
    number_of_taste_cases = int(input())
    for i in range(number_of_taste_cases):
        counter = 0
        first_number, second_number = list(map(int, input().strip().split()))
        while True:
            if first_number % 3 == 0 or second_number % 3 == 0:
                print(0)
                break
            else:
                counter += 1
                if first_number > second_number:
                    first_number = abs(first_number - second_number)
                else:
                    second_number = abs(first_number - second_number)
                if first_number % 3 == 0 or second_number % 3 == 0:
                    print(counter)
                    break

