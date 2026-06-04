class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
print("After changing ", cutting.temperature)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
print(cutting.temperature)

cutting.cup = "small"
print(cutting.cup)

del cutting.cup
print(cutting.size)     #over here we will get an error cause we deleted the cup and there is not attribute in the class

