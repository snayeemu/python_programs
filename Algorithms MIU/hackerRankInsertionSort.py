def insertionSort1(n, arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
            for number in arr:
                print(number, end=" ")
            print()
        arr[i + 1] = key
    for number in arr:
        print(number, end=" ")
    print()
    return arr


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
