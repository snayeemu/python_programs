if __name__ == '__main__':
    given_string = input()
    a, b, c, d, e = 0, 0, 0, 0, 0
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for char in given_string:
        if char.isalnum() and a == 0:
            alnum = True
            a += 1
        if char.isalpha() and b == 0:
            alpha = True
            b += 1
        if char.isdigit() and c == 0:
            digit = True
            c += 1
        if char.islower() and d == 0:
            lower = True
            d += 1
        if char.isupper() and e == 0:
            upper = True
            e += 1

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
