# --------------------------------------------------
# Example 1: Print all even numbers using normal loop

nums = [1,2,3,4,5,6,7,8,9,0]

even_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

print(even_nums)


# --------------------------------------------------
# Example 2: Same using list comprehension

# Syntax:
# [expression for item in iterable if condition]

even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)


# --------------------------------------------------
# Example 3: Square all numbers using list comprehension

nums = [1, 2, 3, 4, 5]

squares = [num * num for num in nums]

print(squares)


# --------------------------------------------------
# Example 4: Convert all strings to uppercase

names = ["sameer", "rahul", "amit"]

upper_names = [name.upper() for name in names]

print(upper_names)


# --------------------------------------------------
# Example 5: Filter numbers greater than 50

nums = [10, 55, 23, 78, 90, 34]

greater_nums = [num for num in nums if num > 50]

print(greater_nums)


# --------------------------------------------------
# Example 6: Replace even numbers with "Even" and odd with "Odd"

nums = [1, 2, 3, 4, 5]

result = ["Even" if num % 2 == 0 else "Odd" for num in nums]

print(result)

# Syntax:
# [value_if_true if condition else value_if_false for item in iterable]


# --------------------------------------------------
# Example 7: Extract first letter from each word

words = ["apple", "banana", "cherry"]

first_letters = [word[0] for word in words]

print(first_letters)


# --------------------------------------------------
# Example 8: Flatten a 2D list (important pattern)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]

print(flattened)


# --------------------------------------------------
# Example 9: Create list of tuples (number and its square)

nums = [1, 2, 3, 4]

pairs = [(num, num*num) for num in nums]

print(pairs)


# --------------------------------------------------
# Example 10: Remove empty strings from list

data = ["apple", "", "banana", "", "cherry"]

cleaned = [item for item in data if item != ""]

print(cleaned)