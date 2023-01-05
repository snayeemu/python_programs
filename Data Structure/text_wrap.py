import textwrap


def wrap(given_string, max_width):
    output = ""
    i = 1
    for char in given_string:
        if i % max_width != 0:
            output += char
        else:
            output += char + "\n"
        i += 1
    return output


if __name__ == '__main__':
    given_string, max_width = input(), int(input())
    result = wrap(given_string, max_width)
    print(result)
