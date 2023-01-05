def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array = [102, 1, 9, 2, 8, 5, 4]
print(bubbleSort(array))
