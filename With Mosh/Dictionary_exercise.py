in_words = {
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
}
phone_number = input("Enter your phone number: ")
i = 0
element = phone_number[i]
# while True:
#     element = phone_number[i]
#     print(in_words[element], " ", end='')
#     i += 1
#     if element == phone_number[-1]:
#         break
for i in phone_number:
    print(in_words.get(i, ""), " ", end='')
