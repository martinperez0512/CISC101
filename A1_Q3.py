"""
This program calculates the subtotal, sales tax, and total of the four items purchased by the end user
Author: Martin Perez
Student Number: 20360377
Date: September 2022
"""
price1 = float(input("Enter price for item 1 "))
price2 = float(input("Enter price for item 2 "))
price3 = float(input("Enter price for item 3 "))
price4 = float(input("Enter price for item 4 "))
subtotal = price1 + price2 + price3 + price4
print("Your Subtotal is $", end="")
print(format(subtotal, '.2f'))
salesTax = subtotal * 0.13
print("Sales Tax $", end="")
print(format(salesTax, '.2f'))
total = subtotal + salesTax
print("Your total is $", end="")
print(format(total, '.2f'))
