# --------------------------------------------------
# Generator Comprehension (Detailed Explanation)

# Generator comprehension looks similar to list comprehension,
# but instead of square brackets [] we use parentheses ()

# List comprehension:
nums = [1, 2, 3, 4]
squares_list = [num * num for num in nums]

print("List comprehension result:", squares_list)

# Generator comprehension:
squares_gen = (num * num for num in nums)

print("Generator object:", squares_gen)
#output: Generator object: <generator object <genexpr> at 0x107791d80>

# --------------------------------------------------
# What is Generator Comprehension?

# A generator comprehension creates a generator object,
# which generates values one by one instead of storing all values in memory.

# Key idea:
# It is memory efficient because values are produced only when needed.


# --------------------------------------------------
# How it works (lazy evaluation)

gen = (i * i for i in range(5))

print("First value:", next(gen))
print("Second value:", next(gen))
print("Third value:", next(gen))

# next() gives next value from generator
# It does NOT store all values like list


# --------------------------------------------------
# Difference between List vs Generator

nums = range(1000000)

# List (takes large memory)
# squares_list = [num * num for num in nums]

# Generator (memory efficient)
squares_gen = (num * num for num in nums)

# Generator is preferred when:
# - working with large data
# - streaming data
# - reading files
# - pipelines


# --------------------------------------------------
# Example 1: Print even numbers using generator

nums = [1, 2, 3, 4, 5, 6]

even_gen = (num for num in nums if num % 2 == 0)

for num in even_gen:
    print("Even number:", num)


# --------------------------------------------------
# Example 2: Sum of squares using generator

nums = [1, 2, 3, 4]

result = sum(num * num for num in nums)

print("Sum of squares:", result)

# Note:
# No need to create list, generator directly used inside sum()


# --------------------------------------------------
# Example 3: Convert words to uppercase using generator

words = ["tea", "coffee", "milk"]

upper_gen = (word.upper() for word in words)

for word in upper_gen:
    print("Upper word:", word)