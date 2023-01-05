if __name__ == "__main__":
    number_of_test_cases1 = int(input())
    for i in range(number_of_test_cases1):
        first_number1, second_number1 = list(map(int, input().strip().split()))[:2]
        if first_number1 > second_number1:
            print(">")
        elif first_number1 < second_number1:
            print("<")
        elif first_number1 == second_number1:
            print("=")

