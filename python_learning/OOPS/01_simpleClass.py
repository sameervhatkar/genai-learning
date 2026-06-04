class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()     #now ginger_tea is an object of class Chai()

print(type(ginger_tea))     #<class '__main__.Chai'>
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)