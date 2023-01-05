given_list = list(map(int, input(" ").strip().split()))
print(given_list)
output = ""
for i in range(len(given_list)):
    if i < (len(given_list) // 2):
        output += str(given_list[i] + given_list[-(i + 1)])
    elif i > len(given_list) // 2:
        break
    else:
        output += str(given_list[i])
        break
print(output)
