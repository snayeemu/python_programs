#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
character = 'H'

#Top Cone
for i in range(thickness):
    print((character * i).rjust(thickness - 1) + character + (character * i).ljust(thickness - 1))

#Top Pillars
for i in range(thickness+1):
    print((character * thickness).center(thickness * 2) + (character * thickness).center(thickness * 6))

#Middle Belt
for i in range((thickness+1)//2):
    print((character * thickness * 5).center(thickness * 6))

#Bottom Pillars
for i in range(thickness+1):
    print((character * thickness).center(thickness * 2) + (character * thickness).center(thickness * 6))

#Bottom Cone
for i in range(thickness):
    print(((character * (thickness - i - 1)).rjust(thickness) + character + (character * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
