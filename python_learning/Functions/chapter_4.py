# ==============================
# PYTHON VARIABLE SCOPE EXAMPLES
# Demonstrates:
# 1. Local Scope
# 2. Global Scope
# 3. Local overriding Global
# 4. Enclosing Scope (Nested Function)
# 5. nonlocal keyword usage
# ==============================


# ==============================
# Example 1: LOCAL SCOPE
# ==============================

def calculate_discount():
    discount = 10   # Local variable (exists only inside this function)
    print("Discount applied:", discount, "%")

calculate_discount()

# print(discount) ❌ ERROR
# This would raise NameError because 'discount'
# is not accessible outside the function


print("\n-----------------------------\n")


# ==============================
# Example 2: GLOBAL SCOPE
# ==============================

tax_rate = 18   # Global variable (accessible throughout program)

def calculate_tax():
    print("Tax rate is:", tax_rate, "%")

calculate_tax()


print("\n-----------------------------\n")


# ==============================
# Example 3: LOCAL VARIABLE OVERRIDES GLOBAL VARIABLE
# ==============================

tax_rate = 18   # Global variable

def calculate_tax_override():
    tax_rate = 5   # Local variable (overrides global inside function only)
    print("Inside function:", tax_rate)

calculate_tax_override()

print("Outside function:", tax_rate)

# Explanation:
# Inside function → Local variable is used
# Outside function → Global variable remains unchanged


print("\n-----------------------------\n")


# ==============================
# Example 4: ENCLOSING SCOPE (Nested Function)
# ==============================

def university():
    department = "Computer Science"   # Enclosing scope variable

    def student():
        # Accessing variable from enclosing function
        department = "Mechanical"
        print("Student belongs to:", department)

    student()
    print("Student belongs to:", department)

university()

# Explanation:
# Inner function accesses variable from outer function
# This is called ENCLOSING SCOPE


print("\n-----------------------------\n")


# ==============================
# Example 5: MODIFY ENCLOSING VARIABLE USING nonlocal
# ==============================

def counter():
    count = 0   # Enclosing scope variable

    def increment():
        nonlocal count   # Allows modification of enclosing variable
        count += 1
        print("Updated count:", count)

    increment()
    increment()

counter()


print("\n-----------------------------\n")


count = 0   # Global variable

def counter():

    count = 10   # Enclosing scope variable (belongs to outer function)

    def increment():

        global count   # Refers to GLOBAL variable (not enclosing one)

        count += 1

        print("Inside inner function:", count)

    increment()

    print("Inside outer function:", count)

counter()

print("Outside function (global):", count)

# ==============================
# SUMMARY: LEGB RULE
# ==============================

# Python searches variables in this order:
# L → Local
# E → Enclosing
# G → Global
# B → Built-in