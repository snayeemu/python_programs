number = int(input())

if number%2 == 1:
    print("Weird")
elif number >= 2 and number <= 5 and number%2 == 0:
    print("Not Weird")
elif number >= 6 and number <= 20 and number%2 == 0:
    print("Weird")
elif number > 20 and number%2 == 0:
    print("Not Weird")