"""
This program takes two integers as parameters and returns the product of the square of each of the parameters
Author: Martin Perez
Student Number: 20360377
Date: Oct 2022
"""
import random


def number_generator():
    """
    this function takes the 2 random number and multiplies the product of their squares
    """
    x = random.randint(1, 3)
    y = random.randint(2, 5)
    print(x * x * y * y)


number_generator()
