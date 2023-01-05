def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > current:
                array[j + 1] = array[j]
            else:
                break
            j -= 1
        array[j + 1] = current
    return array


print(insertionSort([2, 4, 1, 5, 6, 1, 9, 8, 7, 1, 1]))
