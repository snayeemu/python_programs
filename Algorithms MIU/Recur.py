def recur(x):
    print(x)
    if x > 0:
        recur(x - 1)
    print(x)


recur(3)
