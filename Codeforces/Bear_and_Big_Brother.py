if __name__ == "__main__":
    weight_of_limak, weight_of_bob = list(map(int, input().strip().split()))[:2]
    output = 0
    while weight_of_limak <= weight_of_bob:
        weight_of_limak *= 3
        weight_of_bob *= 2
        output += 1
    print(output)
