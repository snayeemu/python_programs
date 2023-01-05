def concatenate(input_list):
    output = ""
    for element in input_list:
        output += element
    return output


if __name__ == "__main__":
    input_list = list(map(str, input("Enter element of list: ").split(" ")))
    output = concatenate(input_list)
    print(output)
