color_list_1 = {"White", "Black", "Red"}
color_list_2 = {"Red", "Green"}
print("Original set elements: ")
print(color_list_1)
print(color_list_2)
print("\nDifferent of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferent of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))

a = ["white","black","green"]
b = ["red","green"]

print("the difference of set is ", set(a) - set(b))
print("the union of set is ", set(a) | set(b))
print("the inntersection of set is ", set(a) & set(b))

def sum(*summation):
    sum = 0
    for i in summation:
        sum = sum + i

    return sum


print(sum(2,4,6,8,5))






