def swap_case(s):
    output = ""
    for char in s:
        if char == char.upper():
            output += char.lower()
        elif char == char.lower():
            output += char.upper()
        else:
            output += char
    return output


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

