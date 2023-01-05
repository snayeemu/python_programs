def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        currentIndex = i
        j = i - 1
        while j >= 0:
            if array[j] > current:
                array[j + 1] = array[j]
                currentIndex = j
            else:
                break
            j -= 1
        array[currentIndex] = current
    return array


array = [1, 3, 2, 5, 4, 11, 20, 11, 2, 1]
print(insertionSort(array))
