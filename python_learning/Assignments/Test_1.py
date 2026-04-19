# --------------------------------------------------
# Assignment 1: Print numbers greater than 40 using for loop and if condition

nums = [12, 45, 67, 23, 90, 34, 50]

for num in nums:
    if num > 40:
        print(num)


# --------------------------------------------------
# Assignment 2: Print numbers NOT divisible by 5 using continue statement

nums = [10, 23, 40, 51, 70, 86]

for num in nums:
    if num % 5 == 0:
        continue
    print(num)


# --------------------------------------------------
# Assignment 3: Print menu items with numbering starting from 1 using enumerate()

menu = ["Tea", "Coffee", "Milk", "Juice"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} {item}")


# --------------------------------------------------
# Assignment 4: Combine two lists and print student marks using zip()

names = ["Aman", "Riya", "Kabir"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")


# --------------------------------------------------
# Assignment 5: Accept numbers from user, skip negative numbers using continue and stop when user enters 0 using break

while True:

    n = int(input("Enter number: "))

    if n < 0:
        continue

    if n == 0:
        break

    print(f"Accepted number: {n}")


# --------------------------------------------------
# Assignment 6: Check whether list contains an even number using for-else loop

numbers = [3, 7, 11, 18, 25]

for num in numbers:

    if num % 2 == 0:
        print("Even number found")
        break

else:
    print("No even number found")


# --------------------------------------------------
# Assignment 7: Print names of students who passed (marks >= 50) using dictionary iteration

students = {
    "Aman": 85,
    "Riya": 92,
    "Kabir": 67,
    "Neha": 48
}

print("Passed students:")

for name, mark in students.items():

    if mark >= 50:
        print(name)