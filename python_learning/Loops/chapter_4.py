#Learning zip() combining 2 lists

names = {"abc", "def", "ghi", "jkl"}
amounts = {40, 50, 120, 70}

for name, amount in zip(names, amounts):
    print(f"{name} paid ₹{amount}")