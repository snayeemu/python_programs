if __name__ == '__main__':
    numbers_of_scores = int(input())
    scores = list(map(int, input().split()))
    maximum_number = scores[0]
    for i in range(len(scores) - 1):
        for j in range (i + 1, len(scores)):
            if scores[i] < scores[j]:
                temp = scores[i]
                scores[i] = scores[j]
                scores[j] = temp

    i = 0
    for element in scores:
        if scores[i] == scores[i + 1]:
            i += 1
        else:
            print(scores[i + 1])
            break