def n_copies(given_string, number_of_copies):
    output = ""
    if len(given_string) < 2:
        for i in range(number_of_copies):
            output += given_string + "\n"
    else:
        for i in range(number_of_copies):
            output += given_string[0] + given_string[1] + "\n"
    return output


if __name__ == "__main__":
    given_string = input("Enter your String: ")
    number_of_copies = int(input("Enter number of copies: "))
    output = n_copies(given_string, number_of_copies)
    print(output)
