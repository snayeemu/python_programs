def count_substring(string, sub_string):
    compare = ""
    count = 0
    for i in range(len(string)):
        compare = string[i: (i + len(sub_string))]
        if compare == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
