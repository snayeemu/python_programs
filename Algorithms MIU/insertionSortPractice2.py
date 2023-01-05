def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        index = i
        j = i - 1
        while j >= 0:
            if array[j] > current:
                array[j + 1] = array[j]
                index = j
            else:
                break
            j -= 1
        array[index] = current
    return array


array = [1, 2, 10, 2, 5, 4, 9, 1, 1, 5]
print(insertionSort(array))
