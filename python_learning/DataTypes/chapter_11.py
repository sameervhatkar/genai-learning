#Dictionary similar to hashmap(key:value)

chai_order = dict(type = "Masala Chai", size = "Large", sugar = 2)
print(f"Chai Order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black_tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe Base: {chai_recipe['base']}")
print(f"Chai Recipe: {chai_recipe}")

del chai_recipe["liquid"]
print(f"Chai Recipe: {chai_recipe}")

#membersihp
print(f"Is sugar is in the order?{'sugar' in chai_order}")

print(f"Order details (keys): {chai_order.keys()}")
#Order details (keys): dict_keys(['type', 'size', 'sugar'])

print(f"Order details (values): {chai_order.values()}")
#Order details (values): dict_values(['Masala Chai', 'Large', 2])

print(f"Order details (items): {chai_order.items()}")
#Order details (items): dict_items([('type', 'Masala Chai'), ('size', 'Large'), ('sugar', 2)])

#removing the last item or we can say removing the last record
last_item = chai_order.popitem()
print(f"Order details (items): {chai_order.items()}")

#If the key is not present lets say we want to fetch the value of key(note) but there is none then we need to use
#get() so that instead of getting the error we can put a message
customer_note = chai_order.get("note", "No Note")
print(customer_note)




