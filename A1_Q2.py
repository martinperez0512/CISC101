"""
This program calculates the amount of force needed to move an object with a provided mass and desired
acceleration
Author: Martin Perez
Student Number: 20360377
Date: September 2022
"""
mass = int(input("Enter the mass of the object (kg) "))
acceleration = float(input("Enter the acceleration rate (m/s/s) "))
force = mass * acceleration
print("To move an object with the mass of", mass, "kg(s), at an acceleration rate of", acceleration,
      "m/s/s, we need a force equal to", format(force, '.1f'), "Newton(s)")
