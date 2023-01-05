from Stack import Stack


def base_converter(decimal_number, base):
    remainder_stack = Stack()
    numbers = "0123456789ABCDEF"
    number_in_new_base = ""
    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(numbers[remainder])
        decimal_number //= base
    while not remainder_stack.is_empty():
        number_in_new_base += remainder_stack.pop()
    return number_in_new_base


print(base_converter(10, 2))
