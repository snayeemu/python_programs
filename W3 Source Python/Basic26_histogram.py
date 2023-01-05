def histogram(character, format_of_histogram):
    for element in format_of_histogram:
        print(character * element)


if __name__ == "__main__":
    character = input("Enter a character to printr: ")
    format_of_histogram = map(int, input("Enter format of histogram: ").split(" "))
    histogram(character, format_of_histogram)
