# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
def is_2000(array):
    for i in range(len(array)):
        if array[i] == 2000:
            return i
        else:
            return -1


monthly_expenses = [2220, 2350, 2600, 2130, 2190]
difference_between_january_and_february = monthly_expenses[1] - monthly_expenses[0]
print(f"In February, {difference_between_january_and_february} dollars I spent extra compare to January")
total_expense_in_first_three_months = 0
for i in range(3):
    total_expense_in_first_three_months += monthly_expenses[i]
print(f"Total expense in first three months of the year is {total_expense_in_first_three_months}")
if is_2000(monthly_expenses) >= 0:
    print(f"Spent exactly 2000 dollar in {is_2000(monthly_expenses) + 1} month")
elif is_2000(monthly_expenses) == -1:
    print("Did not spent exactly 2000 dollar in any month")
print("Is there any 2000 in monthly expenses? \n", 2000 in monthly_expenses)
monthly_expenses.insert(len(monthly_expenses), 1980)
monthly_expenses[3] -= 200
print("After refund expenses in April is", monthly_expenses[3])