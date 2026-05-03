# Convert INR prices to USD

tea_prices_inr = {
    "Masala Chai": 40,
    "Green Chai": 50,
    "Lemon Chai": 60
}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)


# --------------------------------------------------
# Example 1: Increase all prices by 10

tea_prices = {
    "Masala Chai": 40,
    "Green Chai": 50,
    "Lemon Chai": 60
}

updated_prices = {tea: price + 10 for tea, price in tea_prices.items()}

print(updated_prices)


# --------------------------------------------------
# Example 2: Keep only items with price greater than 45

filtered_prices = {tea: price for tea, price in tea_prices.items() if price > 45}

print(filtered_prices)


# --------------------------------------------------
# Example 3: Apply discount (10% off)

discounted_prices = {tea: price * 0.9 for tea, price in tea_prices.items()}

print(discounted_prices)


# --------------------------------------------------
# Example 4: Swap key and value (reverse dictionary)

tea_prices = {
    "Masala Chai": 40,
    "Green Chai": 50
}

reversed_dict = {price: tea for tea, price in tea_prices.items()}

print(reversed_dict)


# --------------------------------------------------
# Example 5: Convert keys to uppercase

tea_prices = {
    "masala chai": 40,
    "green chai": 50
}

upper_keys = {tea.upper(): price for tea, price in tea_prices.items()}

print(upper_keys)


# --------------------------------------------------
# Example 6: Create dictionary from list

names = ["Aman", "Riya", "Kabir"]

# Assign default marks = 0
students = {name: 0 for name in names}

print(students)


# --------------------------------------------------
# Example 7: Create dictionary with squares

nums = [1, 2, 3, 4]

squares = {num: num * num for num in nums}

print(squares)


# --------------------------------------------------
# Example 8: Conditional value transformation

nums = [1, 2, 3, 4, 5]

result = {num: ("Even" if num % 2 == 0 else "Odd") for num in nums}

print(result)


# --------------------------------------------------
# Example 9: Count characters in string

text = "banana"

char_count = {char: text.count(char) for char in text}

print(char_count)


# --------------------------------------------------
# Example 10: Filter dictionary based on key

data = {
    "apple": 10,
    "banana": 20,
    "cherry": 30
}

filtered = {k: v for k, v in data.items() if k.startswith("b")}

print(filtered)