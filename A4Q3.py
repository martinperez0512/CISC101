"""
This program converts Canadian dollars to Chinese Yuan given that one Canadian dollar equals 5.19 Yuan
Author: Martin Perez
Student Number: 20360377
Date: Oct 2022
"""
import random

canadian_dollar = random.randint(1, 1000)


def currency_display():
    """
    This function displays the randomly chosen number that is the value of the Canadian dollar and shows what
    it is equivalent too in Chinese Yuan
    """
    print("$", canadian_dollar, "CAD is equal to ¥", currency_converter(), "CNY")


def currency_converter():
    """
    This function is where the random number is multiplied by the exchange rate and returned to the display function
    """
    result = format(canadian_dollar * 5.19, '.2f')
    return result


currency_display()
