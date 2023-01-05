m, n = list(map(int, input().strip().split()))[:2]

while True:
    r = n % m
    if r == 0:
        print(m)
        break
    else:
        n = m
        m = r
