class Chai:
    origin = "India"        #properties

print(Chai.origin)      #India

Chai.is_hot = True
print(Chai.is_hot)

# Creating object from class chai
masala = Chai()

print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")


masala.is_hot = False
print(f"Masala {masala.is_hot}") 
print(f"Chai Class {Chai.is_hot}") 

masala.flavor = "Masala"
print(f"Flavor: {masala.flavor}")
