def reverseArray(array):
    reverse_array = []
    for i in range(len(array)):
        reverse_array.append(array[-(i + 1)])
    return reverse_array
