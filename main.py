"""
This program prints out a poem with a different persons name each time
Author: Martin Perez
Student Number: 20360377
Date: Oct 2022
"""
import random


def poem():
    """
    This function prints out the poem we want to use and will display whatever is returned from other function
    """
    print("Loops were crazy,")
    print("What are functions about?")
    print(people(), "you can do this")
    print("Just stick it out!")


def people():
    """
    This function contains the list of the names we want to use and will pick a random name
    to return to the poem
    """
    name_list = ["Wendy,", "Al-Barr,", "Faranak,", "Michael,", "Aryan,", "Daniel,", "David,", "Omar,", "Kevin,",
                 "Wanqing,", "Qianran,", "Shupei,", "Hebatalla,", "Chicago,", "Kate,", "Ashton,", "Krishaan,",
                 "Jasmine,", "Steven,", "Han,", "Fredo,", "Tony,", "John,", "Walter"]
    random_choice = random.choice(name_list)  # here a random name is chosen from the list
    return str(random_choice)  # here the chosen name is returned to the poem function


poem()
