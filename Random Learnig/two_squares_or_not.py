import math

if __name__ == "__main__":
    for _ in range(int(input())):
        number = int(input())
        validator = True
        for i in range(int(math.sqrt(number)) + 1):
            x = number - i ** 2
            y = math.sqrt(x)
            if y.is_integer():
                print("Yes")
                validator = False
                break
        if validator:
            print("No")

