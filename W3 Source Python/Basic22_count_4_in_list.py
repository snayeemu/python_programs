def count_four(given_list):
    i = 0
    for element in given_list:
        if element == 4:
            i += 1
    return i


if __name__ == '__main__':
    given_list = map(int, input("Enter elements of list: ").split(" "))
    output = count_four(given_list)
    print(f"Four in given list {output}")
