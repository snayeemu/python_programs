from time import time


def dominant(n):
    result = 0
    for i in range(n):
        result += 1
    return result


start = time()
print(dominant(1000000000))
end = time()
print("Time: ", end - start, "seconds")
