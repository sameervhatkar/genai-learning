def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("black tea", "yes", "low") #positional arguments
#but somtimes we can do this as well
make_chai(tea="green", milk="no", sugar="Medium")   #keywords 

# =====================================================
# CONCEPT: Variable-Length Arguments in Python Functions
#
# This example demonstrates:
# 1. *args  → collects extra positional arguments
# 2. **kwargs → collects extra keyword arguments
#
# These allow a function to accept a flexible number of inputs.
#
# *args  → stored as a tuple
# **kwargs → stored as a dictionary
# =====================================================


def special_chai(*ingredients, **extras):

    # 'ingredients' collects all positional arguments
    # passed to the function after '*'
    # Example: "Cinnamon", "Cardamom"
    # Stored internally as a TUPLE

    print("Ingredients:", ingredients)


    # 'extras' collects all keyword arguments
    # passed using key=value format
    # Example: sweetener="Honey", foam="No"
    # Stored internally as a DICTIONARY

    print("Extras:", extras)


# Function call with:
# 2 positional arguments → go into *ingredients
# 2 keyword arguments → go into **extras

special_chai(
    "Cinnamon",
    "Cardamom",
    sweetener="Honey",
    foam="No"
)


# =====================================================
# OUTPUT:
#
# Ingredients: ('Cinnamon', 'Cardamom')
# Extras: {'sweetener': 'Honey', 'foam': 'No'}
# =====================================================


# =====================================================
# KEY LEARNING POINTS:
#
# *ingredients
# collects positional arguments
# datatype → tuple
#
# **extras
# collects keyword arguments
# datatype → dictionary
#
# Useful when:
# number of inputs is unknown beforehand
# =====================================================

def chai_order(order = []):
    order.append("Masala")
    print(order)

chai_order()
#now what if we accidently call another function again, since list is mutable so it will append the new value
#to existing order list 
#making the order = ["Masala", "Masala"] which we don't want unless its an exception
chai_order()

#resolution
# =====================================================
# CONCEPT: Mutable Default Argument Problem in Python
#
# Default mutable objects like:
# list, dictionary, set
#
# persist across function calls
#
# Solution:
# Use None as default value instead
# =====================================================


def chai_order(order=None):
    # Create a fresh list only if no argument is passed
    if order is None:
        order = []
    order.append("Masala")
    print(f"{order}, {id(order)}")
chai_order()
chai_order()


# --------------------------------------------------
# Example 1: Lambda function for addition of two numbers

add = lambda a, b: a + b

print(add(5, 3))


# --------------------------------------------------
# Example 2: Lambda function to check whether a number is even

is_even = lambda num: num % 2 == 0

print(is_even(4))
print(is_even(7))


# --------------------------------------------------
# Example 3: Lambda function used for sorting a list of students based on marks

students = [
    ("Aman", 85),
    ("Riya", 92),
    ("Kabir", 67)
]

students.sort(key=lambda student: student[1])

print(students)


# --------------------------------------------------
# Example 4: Lambda function used with map() to generate squares of numbers

nums = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, nums))

print(squares)


# --------------------------------------------------
# Example 5: Lambda function used with filter() to keep numbers divisible by 10

nums = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x % 10 == 0, nums))

print(result)


