from area_class import area

if __name__ == "__main__":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area1 = area()
    output = area1.area_of_triangle(base, height)
    print(f"Area of this triangle is: {output}")
