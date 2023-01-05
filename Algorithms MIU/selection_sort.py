def selection_sort(given_list):
    i = 0
    for i in range(len(given_list) - 1):
        j = i + 1
        min_index = i
        while j < len(given_list) :
            if given_list[min_index] > given_list[j]:
                min_index = j
            j += 1
        temp = given_list[i]
        given_list[i] = given_list[min_index]
        given_list[min_index] = temp
    return given_list


test = [9, 2, 4, 5]
print(selection_sort(test))

