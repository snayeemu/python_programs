if __name__ == "__main__":
    given_string = input()
    first_char = given_string[0].upper()
    given_string = first_char + given_string[1:]
    print(given_string)
