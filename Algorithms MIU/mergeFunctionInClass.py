def merge(left, right):
    i, j, k = 0, 0, 0
    merge = [0] * (len(left) + len(right))

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge[k] = left[i]
            i += 1

        else:
            merge[k] = right[j]
            j += 1
        k += 1

        while i < len(left):
            merge[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            merge[k] = right[j]
            j += 1
            k += 1

    return merge


def split(alist):
    mid = len(alist) // 2

    return alist[:mid], alist[mid:]
