if __name__ == '__main__':
    number_of_inputs = int(input())
    integer_list = map(int, input().split())
    new_tuple = tuple(integer_list)
    hash_value = hash(new_tuple)
    print(hash_value)
