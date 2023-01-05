def generate_copies(input_string, number_of_copies):
    copies = ""
    for i in range(number_of_copies):
        copies += input_string + "\n"
    return copies


if __name__ == "__main__":
    input_string = input("Enter your string: ")
    number_of_copies = int(input("Enter how many copy you want: "))
    print(generate_copies(input_string, number_of_copies))
