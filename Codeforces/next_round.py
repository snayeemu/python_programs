if __name__ == "__main__":
    number_of_participants, position = list(map(int, input().strip().split()))[:2]
    scores = list(map(int, input().strip().split()))[:number_of_participants]
    goes_to_next_round = 0
    for i in range(len(scores)):
        if (i < position and scores[i] > 0) or (i > 0 and 0 < scores[i] == scores[i - 1]):
            goes_to_next_round += 1
        else:
            break
    print(goes_to_next_round)
