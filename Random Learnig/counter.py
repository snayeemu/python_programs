from array import array
from collections import Counter

if __name__ == '__main__':
    exampleList = [7,6,5,4,7,8,6,5,7,8,6,8]
    counts = Counter (exampleList)
    # array = list(counts)
    # print (counts)
    # print(array)

    specific = counts[7]
    print(specific)

    noneExist = counts[55]
    print (noneExist)

    counts[7] = 15
    print (counts[7])
    # print(counts)
    # print(exampleList)

    # counts [7] = 0

    # print(counts)

    # del counts[7]

    # print(counts)

    x = list(counts.elements())

    print(x)

    y = counts.most_common(3)

    # print(y)

    anotherList = [6,6,6,8,87,9,9,86,5,8]

    counts2 = Counter(anotherList) # have to use --> .most_common for getting list according to most reapeted items
    print(counts2)

    list = list(counts2.most_common())
    # most reapeted in anotherList array is
    print(list[0][0])
    # print(list)

    z = counts - counts2

    print(z)