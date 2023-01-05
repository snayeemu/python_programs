if __name__ == '__main__':
    name_and_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_and_score.append([name, score])
    lowest = name_and_score[0][1]
    second_lowest = 100.0
    for colum in name_and_score:
        if lowest > colum[1]:
            lowest = colum[1]
    for colum in name_and_score:
        if second_lowest > colum[1] > lowest:
            second_lowest = colum[1]
    second_lowest_names = []
    for colum in name_and_score:
        if colum[1] == second_lowest:
            second_lowest_names.append(colum[0])
    second_lowest_names.sort()
    for element in second_lowest_names:
        print(element)
