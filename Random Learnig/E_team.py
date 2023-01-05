if __name__ == "__main__":
    number_of_problems = int(input())
    number_of_problems_will_be_implement = 0
    for i in range(number_of_problems):
        counter = 0
        number_of_solution = list(map(int, input().strip().split()))[:3]
        for number in number_of_solution:
            counter += number
        if counter >= 2:
            number_of_problems_will_be_implement += 1
    print(number_of_problems_will_be_implement)

