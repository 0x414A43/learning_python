#!/bin/python3

#name = input("Enter your name: ")
#drink = input("Whats your favorite drink: ")
#print("Hello " +name+" ! Have a "+drink+".")

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me a another number: "))

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "/":
    print(x / y)
elif o == "*":
    print(x * y)
elif o == "**" or o == "^":
    print(x ** y)

else:
    print("Unknown Operator")