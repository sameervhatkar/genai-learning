class Chaicup:
    size = 150      #ml

    #implementing the method in the class
    def describe(self):
        return f"A {self.size}ml chai cup"
    
cup = Chaicup()
print(cup.describe())

#print(Chaicup.describe())
#TypeError: Chaicup.describe() missing 1 required positional argument: 'self' 
#So we need to pass the reference cause the describe method is expecting the arguments i.e....
print(Chaicup.describe(cup))