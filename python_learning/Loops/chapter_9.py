# List of users
# Each user is represented as a dictionary
# Dictionary stores:
# id → user identifier
# total → total purchase amount
# coupon → coupon code applied by the user

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"}
]


# Dictionary storing coupon discount details
# Key → coupon code
# Value → tuple(percent_discount, fixed_discount)

# Example:
# "P20": (0.2, 0)
# means 20% discount and no fixed discount

discounts = {
    "P20": (0.2, 0),
    "F10": (0.0, 10),
    "P50": (0.5, 0)
}


# Loop through each user in the users list
for user in users:

    # Fetch discount details from dictionary using coupon code
    # user["coupon"] gets coupon value from current user dictionary

    # discounts.get(key, default_value)
    # If coupon exists → returns tuple(percent, fixed)
    # If coupon does NOT exist → returns default (0, 0)

    percent, fixed = discounts.get(user["coupon"], (0, 0))


    # Calculate total discount amount
    # Formula:
    # discount = (total_amount * percent_discount) + fixed_discount

    discount_amount = user["total"] * percent + fixed


    # Print final result
    # Showing:
    # user id
    # total purchase amount
    # discount received

    print(f"{user['id']} paid {user['total']} and got a discount of {discount_amount}")