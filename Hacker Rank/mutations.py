def mutate_string(given_string, index_to_insert, character_to_insert):
    given_string = given_string[:index_to_insert] + character_to_insert + given_string[(index_to_insert + 1):]
    return given_string


if __name__ == '__main__':
    given_string = input()
    index_to_insert, character_to_insert = input().split()
    new_string = mutate_string(given_string, int(index_to_insert), character_to_insert)
    print(new_string)
