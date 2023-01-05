"""
Task:
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.


Input format:
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.


Output format:
Print the amount of money earned


Sample input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50


Sample output:
200

"""


def earned_money(size_of_shoes, desired_size_and_price):
    earned = 0
    for colum in desired_size_and_price:
        for element in size_of_shoes:
            if colum[0] == element:
                size_of_shoes.remove(element)
                earned += colum[1]
                break
    return earned


if __name__ == "__main__":
    number_of_shoes = int(input())
    size_of_shoes = list(map(int, input().strip().split(" ")))[:number_of_shoes]
    number_of_customers = int(input())
    desired_size_and_price = []
    for i in range(number_of_customers):
        desired_size_and_price.append(list(map(int, input().strip().split(" ")))[:2])
    earned = earned_money(size_of_shoes, desired_size_and_price)
    print(earned)
