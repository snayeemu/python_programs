def sum(first_number, second_number, third_number):
    if first_number == second_number == third_number:
        return first_number * 3 * 3
    else:
        return first_number + second_number + third_number


if __name__ == '__main__':
    print(sum(3, 3, 2))
