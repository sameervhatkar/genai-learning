# age = int(input("Enter you age: "))
# if(age >= 18):
#     print("Can Vote")
# else:    
#     print("Need to wait ", 18 - age, " years.")

#Looping
# for i in range(5+1):
#     print(i)

#Functions

# def display(name):
#     print("Hello ", name)

# name = input("Enter your name: ")
# display(name)

# def add(a, b):
#     return a + b

# a = int(input())
# b = int(input())
# print(add(a, b))

#-------------------Mini Task-----------------

from datetime import date


def greet(name, birthYear):
    print("Hello ", name, " you are ", int(date.today().year) - birthYear, " years old")
    
name = input("Enter your name: ")
birthYear = int(input("Enter your Birth Year"))
greet(name, birthYear)

