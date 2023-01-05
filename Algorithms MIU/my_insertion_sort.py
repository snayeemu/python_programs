def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while array[j] > current and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


array = [9, 8, 5, 6, 2, 8, 7]
insertion_sort(array)
print(array)
