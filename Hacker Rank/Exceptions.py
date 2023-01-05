if __name__ == "__main__":
    number_of_test_cases = int(input())
    for i in range(number_of_test_cases):
        first_number, second_number = list(map(str, input().strip().split()))[:2]
        try:
            print(int(first_number) // int(second_number))
        except (ZeroDivisionError, ValueError) as e:
            print(f"Error Code: {e}")
