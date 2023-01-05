product1 = input()
product2 = input()
product1 = product1.split()
product2 = product2.split()
cost_of_product1 = int(product1[1]) * float(product1[2])
cost_of_product2 = int(product2[1]) * float(product2[2])
final_cost = cost_of_product1 + cost_of_product2
print("valor a pagar: R$ %.2f" % final_cost)
