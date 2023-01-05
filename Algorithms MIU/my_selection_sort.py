def selectionSort(array):
    for i in range(len(array)):
        minValue = array[i]
        index = i
        for j in range((i + 1), len(array)):
            if minValue > array[j]:
                minValue = array[j]
                index = j
        array[i], array[index] = minValue, array[i]
    return array


array = [3, 4, 1, 6, 8, 10, 1, 2]
selectionSort(array)
print(array)









# temp = array[i]
# array[i] = minValue
# array[index] = temp