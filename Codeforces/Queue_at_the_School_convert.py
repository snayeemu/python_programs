number_of_children, time = list(map(int, input().strip().split()))[:2]
initial_arrangement = list(input())

for j in range(time):
    i = 0
    while i < (number_of_children - 1):
        i += 1
        if initial_arrangement[i] == "G" and initial_arrangement[i - 1] == "B":
            initial_arrangement[i] = "B"
            initial_arrangement[i - 1] = "G"
            i += 1

initial_arrangement = "".join(initial_arrangement)
print(initial_arrangement)
