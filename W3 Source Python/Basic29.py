def print_out_colors_set(color_list1, color_list2):
    output = "{"
    for element in color_list1:
        try:
            color_list2.index(element)
        except ValueError:
            output += "'" + str(element) + "', "
    output = output[::-1]
    output = output.replace(",", "}", 1)
    output = output[::-1]
    return output


if __name__ == "__main__":
    color_list_1 = ["White", "Black", "Red"]
    color_list_2 = ["Red", "Green"]
    output = print_out_colors_set(color_list_1, color_list_2)
    print(output)


