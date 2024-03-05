"""
This program prints out the total number of cupcakes that need to be baked for the study group
Author: Martin Perez
Student Number: 20360377
Date: September 2022
"""
people = int(input("how many people will be attending? "))
pets = int(input("how many of the people attending own pets? "))
cakes4People = people * 2
total = cakes4People + pets + 4
print(total, "Cupcakes need to be baked")
