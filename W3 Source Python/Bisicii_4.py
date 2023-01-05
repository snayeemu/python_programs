def uniqueTriple(given_list):
    output = []
    for i in range(len(given_list) - 2):
        if given_list[i] + given_list [i + 1] + given_list[i + 2] == 0:
            output.append((given_list[i], given_list[i + 1], given_list[i + 2]))
    return output


if __name__ == "__main__":
    x = [1, -6, 4, 2, -1, 2, 0, -2, 0]
    output = uniqueTriple(x)
    print(output)
