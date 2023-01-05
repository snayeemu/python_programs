def selection_sort(array):
    for i in range(len(array) - 1):
        minIndex = i
        minValue = array[i]
        for j in range(i, len(array)):
            if array[j] < minValue:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]

    return array


print(selection_sort([2, 1, 0, 6, 9, 10, 9, 2]))
