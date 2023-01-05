weight = float(input("Enter weight: "))
unit = input("(K)gs or (L)bs: ")
if unit.upper() == ("K"):
    print("Weight in Lgs is: %.2f" %(weight * 2.20462))
elif unit.upper() == ("L"):
    print("Weight in Kbs is: %.2f" %(weight / 2.20462))