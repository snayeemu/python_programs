def return_string_with_is(input_string):
    if len(input_string) >= 2 and input_string[0] == "i" and input_string[1] == "s":
        return input_string
    else:
        return "is " + input_string
