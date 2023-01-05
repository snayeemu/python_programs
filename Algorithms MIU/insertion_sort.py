def insertion_sort(given_array):
    for j in range(1, len(given_array)):
        key = given_array[j]
        i = j - 1
        while i >= 0 and given_array[i] > key:
            given_array[i + 1] = given_array[i]
            i = i - 1
        given_array[i + 1] = key
    return given_array


array = [7, 3, -10, 1, 13, 6, 4, -5]
print(insertion_sort(array))
