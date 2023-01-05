if __name__ == "__main__":
    number_of_students, time = list(map(int, input().strip().split()))[:2]
    initial_arrangement = list(input())
    check = None
    for i in range(time):
        for j in range(len(initial_arrangement) - 1):
            if initial_arrangement[j] == "B" and initial_arrangement[j + 1] == "G" and check != j:
                check = j + 1
                initial_arrangement[j] = "G"
                initial_arrangement[j + 1] = "B"
    initial_arrangement = "".join(initial_arrangement)
    print(initial_arrangement)
