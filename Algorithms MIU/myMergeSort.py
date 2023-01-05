def mergeSort(array):
    if len(array) <= 1:
        return
    else:
        mid = len(array) // 2
        left = array[0:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        addToSortedArray(left, right, array)


def addToSortedArray(left, right, array):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


array = [3, 2, 1, 8, 9, 6, 5]
mergeSort(array)
print(array)
