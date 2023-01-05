def get_sum(a, b):
    a = 1 if a == 11 and b != 11 else a
    b = 1 if b == 11 else b
    sum_ab = a + b
    if sum_ab <= 21:
        return sum_ab
    else:
        return 0


if __name__ == "__main__":
    a, b = list(map(int, input().strip().split()))
    print(get_sum(a, b))
