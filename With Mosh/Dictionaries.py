customer = {
    "name": "John Smith",
    "age": 30,
    # "age": 40 --> not allowed
    "is_verified": True
}
customer["name"] = "Nayeem"
customer["birthdate"] = "07, 12, 2000"
print(customer["name"])
print(customer.get("birthdate)"))  # do not throw error if key does not exist

