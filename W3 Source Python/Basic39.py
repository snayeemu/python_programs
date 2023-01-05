if __name__ == "__main__":
    principle_amount = float(input("Enter principle amount: "))
    probable_benefit_rate = float(input("Enter the rate of probable benefit: "))
    years = int(input("Years: "))
    expected_amount = principle_amount
    for i in range(years):
        expected_amount += (probable_benefit_rate * expected_amount) / 100
    print("Expected amount: %.2f" % expected_amount)
