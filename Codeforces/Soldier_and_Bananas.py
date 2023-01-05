if __name__ == "__main__":
    value_per_unit, initial_number_of_dollars, number_of_bananas = list(map(int, input().strip().split()))[:3]
    total_amount = 0
    for i in range(1, number_of_bananas + 1):
        total_amount += i * value_per_unit
    borrow = total_amount - initial_number_of_dollars if total_amount > initial_number_of_dollars else 0
    print(borrow)
