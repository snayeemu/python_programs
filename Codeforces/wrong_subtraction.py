if __name__ == "__main__":
    number, subtractions_time = list(map(int, input().strip().split()))[:2]
    for i in range(subtractions_time):
        if number % 10 == 0:
            number //= 10
        else:
            number -= 1
    print(number)
