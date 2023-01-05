import random

if __name__ == "__main__":
    char_list = ['a', 'e', 'i', 'o', 'u']
    random.shuffle(char_list)
    print(''.join(char_list))
    print(char_list)
