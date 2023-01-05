def vowel_or_not(character):
    if character.upper() == "A" or character.upper() == "E" or character.upper() == "I" or character.upper() == "O" or character.upper() == "U":
        return "vowel"
    else:
        return "not vowel"


if __name__ == "__main__":
    character = input("Enter a character: ")
    output = vowel_or_not(character)
    print(output)
