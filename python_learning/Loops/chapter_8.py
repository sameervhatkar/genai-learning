#assign value AND use it inside an expression at the same time :=(walrus operator)


while (user_input := input("Enter a number (type exit to stop): ")) != "exit":
    print("You entered:", user_input)

#another example
numbers = [10, 20, 30, 40]

if (length := len(numbers)) > 3:
    print("List has", length, "elements")



