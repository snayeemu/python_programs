if __name__ == "__main__":
    upper_case_letter = 0
    lower_case_letter = 0
    word = input()
    for char in word:
        if char.isupper():
            upper_case_letter += 1
        elif char.isalpha():
            lower_case_letter += 1
    if upper_case_letter > lower_case_letter:
        word = word.upper()
    else:
        word = word.lower()
    print(word)
