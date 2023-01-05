def find_max(list):
    max = list[0]
    for element in list:
        if max < element:
            max = element
    return max