# --------------------------------------------------

# Example 1: Remove duplicates using set comprehension

nums = [1, 2, 3, 4, 3, 5, 6, 1, 4]

# Set automatically removes duplicates

unique_num = {num for num in nums}

print(unique_num)

# --------------------------------------------------

# Example 2: Extract unique values from dictionary of sets

# Dictionary where each key has a set of values

data = {

    "A": [1, 2, 3],

    "B": [3, 4, 5],

    "C": [5, 6, 7]

}

# Goal: get all unique values across all sets

unique_values = {value for values in data.values() for value in values}

print(unique_values)


# Explanation:

# Loop through each set → then each value → collect unique values

# --------------------------------------------------

# Example 3: Get only even numbers from list using set comprehension

nums = [1, 2, 3, 4, 5, 6, 7, 8]

even_nums = {num for num in nums if num % 2 == 0}

print(even_nums)

# --------------------------------------------------

# Example 4: Square all numbers (set version)

nums = [1, 2, 3, 4]

squares = {num * num for num in nums}

print(squares)

# Note:

# Output is unordered because sets are unordered

# --------------------------------------------------

# Example 5: Convert list of strings to uppercase (unique results only)

names = ["sameer", "rahul", "amit", "sameer"]

upper_names = {name.upper() for name in names}

print(upper_names)

# Duplicate "sameer" removed automatically

# --------------------------------------------------

# Example 6: Extract first letters (unique only)

words = ["apple", "banana", "cherry", "apricot"]

first_letters = {word[0] for word in words}

print(first_letters)

# --------------------------------------------------

# Example 7: Flatten a 2D list into unique values

matrix = [

    [1, 2, 3],

    [2, 3, 4],

    [4, 5, 6]

]

flattened_unique = {num for row in matrix for num in row}

print(flattened_unique)

# --------------------------------------------------

# Example 8: Filter strings with length greater than 5

words = ["apple", "banana", "cherry", "kiwi"]

long_words = {word for word in words if len(word) > 5}

print(long_words)

# --------------------------------------------------

# Example 9: Remove vowels from a string and keep unique characters

text = "programming"

result = {char for char in text if char not in "aeiou"}

print(result)

# --------------------------------------------------

# Example 10: Create set of tuples (number and its square)

nums = [1, 2, 3, 4]

pairs = {(num, num*num) for num in nums}

print(pairs)