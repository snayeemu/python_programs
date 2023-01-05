if __name__ == "__main__":
    a, b = list(map(int, input().strip().split()))[0:2]
    mySum = 0
    while a <= b:
        mySum += a ** 2
        a += 1
    print(mySum)
