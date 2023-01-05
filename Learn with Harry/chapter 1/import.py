import math
print(math.cos(3.65))
print(math.floor(3.65))
a = 1
b = 3
print (a + b)
c = "This is me"
d = 3.4
print(c)
print(type(a))

str1 = "this is my python string"
print(str1.capitalize())
print(str1.find("this"))
print(str1.upper())
items = [1, 2, 3]
print(items)
print(type(items))
newItem = ["harry", 2, 3]
print(newItem) 
newItem[0] = "Nayeem"
print(type(newItem))
print(newItem)
tup1 = (1,2,3)
#can not be changed

dict1 = {}
print(type(dict1))
print(dict1)

dict1["virat"] = 100
dict1["sachin"] = 500
print(dict1["sachin"])
print(dict1.get("virat"))
print(dict1.keys())

list1 = [1, 2, 3, 4, 4, 1]
s1 = set(list1)
print(s1)

a = 5
b = 10
c = "Harry"
print(str(a) + str(b) + c)
print("10 - 5 is ", 10-5)
print("10 / 5 is ", 10/5)
print("10 * 5 is ", 10*5)
print("10 + 5 is ", 10+5)
'''var = int(input())
print(var)

if (var > 4):
    print("Variable is greater")
elif (var == 2):
    print("Variable is two")
else:
    print("Varable is not greater")
'''
for i in range(0, 101):
    print(i)
print("\n\n")
i = 0
while ( i < 101 ):
    print(i)
    i += 1

def average(num1, num2):
    avr = (num1 + num2) / 2
    return avr

print(average(3,6))

index = 3
try:
    print(index)

except Exception as e:
    print(e)

# f = open("1.txt", "w")
# f.write("Subscribe this channel for more")
# f.close
f = open("1.txt", "r")
content = f.read()
f.close()
print(content)