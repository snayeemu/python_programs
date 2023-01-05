import math

if __name__ == "__main__":
    no_of_test_cases = int(input())
    for i in range(1, no_of_test_cases + 1):

        a, b, c = list(map(int, input().strip().split()))[:3]
        print("Case %d: " % i, end='')
        print("Yes" if c % math.gcd(max(a, b), min(a, b)) == 0 else "No")
