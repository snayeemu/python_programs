# first method for encoding
def encode_rot(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for char in text:
        if char.isupper() and char.isalpha():
            result += Alphabet[(Alphabet.index(char) + key) % 26]

        elif not char.isupper() and char.isalpha():
            result += alphabet[(alphabet.index(char) + key) % 26]

        else:
            result += char
    return result


# second method for decoding
def decode_rot(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for char in text:
        if char.isupper() and char.isalpha() and Alphabet.index(char) >= 13:
            result += Alphabet[(Alphabet.index(char) - key)]

        elif not char.isupper() and char.isalpha() and alphabet.index(char) >= 13:
            result += alphabet[(alphabet.index(char) - key)]

        elif char.isupper() and char.isalpha() and Alphabet.index(char) < 13:
            result += Alphabet[26 - abs((Alphabet.index(char) - key))]

        elif not char.isupper() and char.isalpha() and alphabet.index(char) < 13:
            result += alphabet[26 - abs((alphabet.index(char) - key))]

        else:
            result += char
    return result


print("After encoding: ", end='')
encode_output = encode_rot("Hello World!", 13)
print(encode_output)
print("After encoding: ", end='')
decode_output = decode_rot("Uryyb Jbeyq!", 13)
print(decode_output)
