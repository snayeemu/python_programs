if __name__ == "__main__":
    punched_with_frying_pan = int(input())
    shut_into_balcony_door = int(input())
    paws_trampled_with_heels = int(input())
    call_her_mom = int(input())
    total_dragon = int(input())
    i = 1
    number_of_damaged_dragon = 0
    while i <= total_dragon:
        if i % punched_with_frying_pan == 0 or i % shut_into_balcony_door == 0 or i % paws_trampled_with_heels == 0 or\
                i % call_her_mom == 0:
            number_of_damaged_dragon += 1
        i += 1
    print(number_of_damaged_dragon)
