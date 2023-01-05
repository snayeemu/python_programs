def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 != year % 100):
        return True
    else:
        return False


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))

