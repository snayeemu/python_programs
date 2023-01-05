"""
Name: MD: Gausul Azam
Batch: 49
ID: 1848CSE00733
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return
    theValueOfMidIndex = len(arr) // 2
    theLeftArray = arr[:theValueOfMidIndex]
    theRightArray = arr[theValueOfMidIndex:]

    merge_sort(theLeftArray)
    merge_sort(theRightArray)

    mergingTwoAray(theLeftArray, theRightArray, arr)


def mergingTwoAray(a, b, arr):
    lenOfTheArray_a = len(a)
    lenOfTheArray_b = len(b)
    indexForArray_a = indexOfArray_b = indexForTheFinalSortedArray = 0

    while indexForArray_a < lenOfTheArray_a and indexOfArray_b < lenOfTheArray_b:
        if a[indexForArray_a] <= b[indexOfArray_b]:
            arr[indexForTheFinalSortedArray] = a[indexForArray_a]
            indexForArray_a += 1
            indexForTheFinalSortedArray += 1
        else:
            arr[indexForTheFinalSortedArray] = b[indexOfArray_b]
            indexOfArray_b += 1
            indexForTheFinalSortedArray += 1

    while indexForArray_a < lenOfTheArray_a:
        arr[indexForTheFinalSortedArray] = a[indexForArray_a]
        indexForArray_a += 1

    while indexOfArray_b < lenOfTheArray_b:
        arr[indexForTheFinalSortedArray] = b[indexOfArray_b]
        indexOfArray_b += 1
        indexForTheFinalSortedArray += 1


if __name__ == "__main__":
    myArrayForPassingAsParameterToBeSorted = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(myArrayForPassingAsParameterToBeSorted)
    print(myArrayForPassingAsParameterToBeSorted)
