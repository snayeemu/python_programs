def selectionSort(array):
    for i in range(len(array)):
        minValue = array[i]
        minIndex = i
        for j in range(i, len(array)):
            if minValue > array[j]:
                minValue = array[j]
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array


array = [1, 9, 4, 2, 5, 7, 8, 5, 3, 8, 2]
print(selectionSort(array))
