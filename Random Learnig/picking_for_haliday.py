if __name__ == "__main__":
    number_of_inputs1 = int(input())
    for i in range(number_of_inputs1):
        length1, width1, height1 = list(map(int, input().strip().split()))[:3]
        if length1 <= 20 and width1 <= 20 and height1 <= 20:
            print(f"Case {i + 1}: good")
        else:
            print(f"Case {i + 1}: bad")
