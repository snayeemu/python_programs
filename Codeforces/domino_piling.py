if __name__ == "__main__":
    m, n = list(map(int, input().strip().split()))[:2]
    area = m * n
    number_of_domino = area // 2
    print(number_of_domino)
