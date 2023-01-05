def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        index = i
        while j >= 0:
            if array[j] > current:
                array[j + 1] = array[j]
                index = j
            j -= 1
        array[index] = current
    return array


print(insertionSort([2, 1, 5, 4, 3, 10, 5, 3]))
