if __name__ == "__main__":
    number, colors = int(input()), input()
    output = 0
    for i in range(number - 1):
        if colors[i] == colors[i + 1]:
            output += 1
    print(output)
