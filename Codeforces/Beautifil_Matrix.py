if __name__ == "__main__":
    matrix = []
    for _ in range(5):
        row = list(map(int, input().strip().split()))[:5]
        matrix.append(row)
    i = 0
    output = None
    for row in matrix:
        i += 1
        j = 0
        for number in row:
            j += 1
            if number == 1:
                output = abs(3 - i) + abs(3 - j)
    print(output)
