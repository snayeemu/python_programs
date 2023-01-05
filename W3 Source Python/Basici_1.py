def test_data(data):
    if len(data) == len(set(data)):
        return True
    return False


if __name__ == "__main__":
    print(test_data([1, 5, 7, 9]))
    print(test_data([2, 4, 5, 5, 7, 9]))