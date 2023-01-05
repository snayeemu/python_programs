def average(all_heights):
    unique_heights = set(all_heights)
    sum_of_unique_heights = 0
    length_of_unique_heights = len(unique_heights)
    for element in unique_heights:
        sum_of_unique_heights += element
    average_height = sum_of_unique_heights / length_of_unique_heights
    return "%.3f" % average_height


if __name__ == '__main__':
    number_of_inputs = int(input())
    all_heights = list(map(int, input().strip().split()))[:number_of_inputs]
    result = average(all_heights)
    print(result)
