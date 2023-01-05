if __name__ == "__main__":
    number_of_stops = int(input())
    minimum_seat_needed = 0
    people_in_tram = 0
    for i in range(number_of_stops):
        passenger_exited, passenger_entered = list(map(int, input().strip().split()))[:2]
        people_in_tram -= passenger_exited
        people_in_tram += passenger_entered
        if people_in_tram > minimum_seat_needed:
            minimum_seat_needed = people_in_tram
    print(minimum_seat_needed)
