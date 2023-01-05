import math

if __name__ == "__main__":
    x1, y1 = list(map(float, input("Enter x1 and y1: ").strip().split()))[:2]
    x2, y2 = list(map(float, input("Enter x2 and y2: ").strip().split()))[:2]
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    print("Distance is: %.2f" % distance)
