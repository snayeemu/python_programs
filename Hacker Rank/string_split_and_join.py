

def split_and_join(given_string):
    given_string = given_string.split(" ")
    given_string = "-".join(given_string)
    return given_string


if __name__ == '__main__':
    given_string = input()
    result = split_and_join(given_string)
    print(result)
