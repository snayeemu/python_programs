if __name__ == "__main__":
    coordinate_of_the_house = int(input())
    steps = 0
    while coordinate_of_the_house != 0:
        if coordinate_of_the_house >= 5:
            coordinate_of_the_house -= 5
        else:
            coordinate_of_the_house = 0
        steps += 1
    print(steps)
