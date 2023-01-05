if __name__ == "__main__":
    numberOfWords = int(input())
    for i in range(numberOfWords):
        given_number = input()
        if len(given_number) == 5:
            print(3)
        elif (given_number[0] == 'o' and given_number[1] == 'n') or (given_number[0] == 'o' and given_number[2] == 'e') or (given_number[1] == 'n' and
                                                                                                                            given_number[2] == 'e'):
            print(1)
        else:
            print(2)

