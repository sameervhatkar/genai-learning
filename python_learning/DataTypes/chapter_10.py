#Sets

essential_spices = {"cardomom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black_pepper"}

#Union
all_spices = essential_spices | optional_spices
print(f"Union of all spices: {all_spices}")
#output: Union of all spices: {'ginger', 'cloves', 'cardomom', 'black_pepper', 'cinnamon'}

common_spices = essential_spices & optional_spices
print(f"Intersection of all spices: {common_spices}")
#Intersection of all spices: {'ginger'}

#same for set difference and membership

#frozenSet it frozes the set
