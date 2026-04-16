order_amount = int(input("Enter the order amount: "))
#Usage of ternary Operator
delivery_fees = 0 if order_amount > 300 else 30
print(f"The delivery amount is {delivery_fees}")