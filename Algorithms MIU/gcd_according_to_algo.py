m, n = list(map(int, input().strip().split()))[:2]

while True:
    r = m % n
    if r == 0:
        print(n)
        break
    else:
        m = n
        n = r
