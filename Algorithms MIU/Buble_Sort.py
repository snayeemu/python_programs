def Bubble_Sort(given_array):
    for i in range(len(given_array) - 1):
        for j in range(len(given_array) - 1):
            if given_array[j + 1] < given_array[j]:
                temp = given_array[j + 1]
                given_array[j + 1] = given_array[j]
                given_array[j] = temp
    return given_array


arr = [12, 7, 9, 1, 3, 73, 11, 15, 62, 19]
print(Bubble_Sort(arr))
