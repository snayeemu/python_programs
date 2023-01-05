if __name__ == "__main__":
    name = input()
    distinct_char = set(name)
    if len(distinct_char) % 2 == 1:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
