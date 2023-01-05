def gcd(first_number, second_number):
    range_counter = first_number if first_number < second_number else second_number
    if first_number == 0 or second_number == 0:
        return abs(first_number + second_number)
    for i in range(range_counter, 0, -1):
        if first_number % i == 0 == second_number % i:
            return i


if __name__ == "__main__":
    simons_number, antisimons_number, total_stones = list(map(int, input().strip().split()))[:3]
    i = 1
    while True:
        if i % 2 == 1:
            stones_taken = gcd(simons_number, total_stones)
            if total_stones >= stones_taken:
                total_stones -= stones_taken
            else:
                print(1)
                break
        else:
            stones_taken = gcd(antisimons_number, total_stones)
            if total_stones >= stones_taken:
                total_stones -= stones_taken
            else:
                print(0)
                break
        i += 1


