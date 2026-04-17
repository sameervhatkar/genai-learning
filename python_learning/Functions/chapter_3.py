#each cup of chai is costing around ₹15, so generate the bill

def calculate_bill(number_of_cups):
    return number_of_cups * 15

number_of_cups = int(input("How many cups you had? "))
total = calculate_bill(number_of_cups)
print(f"The bill is ₹{total} in which you had {number_of_cups} number of cups each costing ₹15.")