def selectionSort(array):
    for i in range(len(array) - 1):
        minNumber = array[i]
        minIndex = i
        for j in range(i, len(array)):
            if array[j] < minNumber:
                minNumber = array[j]
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array


print(selectionSort([1, 3, 5, 2, 5, 1, 3, 10]))
