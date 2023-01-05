if __name__ == "__main__":
    length_of_ticket_number = int(input())
    ticket_number = input()[:length_of_ticket_number]
    first_half_counter = (length_of_ticket_number // 2) - 1
    sum_of_first_half = 0
    sum_of_second_half = 0
    validator = False
    for i in range(length_of_ticket_number):
        if int(ticket_number[i]) == 4 or int(ticket_number[i]) == 7:
            pass
        else:
            break
        if i <= first_half_counter:
            sum_of_first_half += int(ticket_number[i])
        else:
            sum_of_second_half += int(ticket_number[i])
        if i == length_of_ticket_number - 1 and sum_of_first_half == sum_of_second_half:
            validator = True
    if validator:
        print("YES")
    else:
        print("NO")
