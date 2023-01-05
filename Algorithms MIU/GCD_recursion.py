def GCD(n, m):
    if n < m:
        return GCD(m, n)
    if n >= m and n % m == 0:
        return m
    else:
        return GCD(m, n % m)

