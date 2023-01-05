from logging import exception


if __name__ == '__main__':
    result = []
    first_number = int(input())
    second_number = int(input())
    third_number = int(input())
    exception = int(input())
    
    for i in range(first_number + 1):
        for j in range(second_number + 1):
            for k in range(third_number + 1):
                if i + j + k != exception:
                    result.append([i, j, k])
    print(result)