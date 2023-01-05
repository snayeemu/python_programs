if __name__ == "__main__":
    number = input()
    counter = 0
    for digit in number:
        if int(digit) == 4 or int(digit) == 7:
            counter += 1
    if counter == 4 or counter == 7:
        print("YES")
    else:
        print("NO")
