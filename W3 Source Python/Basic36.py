def add(first_object, second_object):
    if isinstance(first_object, int) and isinstance(second_object, int):
        return first_object + second_object
    else:
        return "objects have to be integer"


if __name__ == "__main__":
    print(add(5, 5))
    print(add(5, "5"))
    