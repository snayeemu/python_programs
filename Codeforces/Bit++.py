if __name__ == "__main__":
    output = 0
    for _ in range(int(input())):
        bit = input()
        if bit.find("++") != -1:
            output += 1
        else:
            output -= 1
    print(output)
