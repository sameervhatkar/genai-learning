#Learning for-else

# for item in sequence:
#     if condition:
#         break
# else:
#     runs if loop completes normally

numbers = {2, 4, 6, 8, 10}
search = int(input("Enter a number to be searched: "))
for number in numbers:
    if number == search:
        print("Number found")
        break

else:
    print("Number not found.")