"""
This program is a menu that allows the user to choose which of the 3 previous function programs to execute
Author: Martin Perez
Student Number: 20360377
Date: Oct 2022
"""
import random


def menu():
    """
    This function displays the menu of choices and depending on the choice will run a separate function
    """
    choice = int(input("Which function would you like to execute?\n Click 1 for poem with random names.\n "
                       "Click 2 for the integer calculator.\n Click 3 for the CAD to CNY converter. "))
    if choice == 1:
        print("You have chosen option 1, the poem")
        poem()
    if choice == 2:
        print("You have chosen option 2, the number generator")
        number_generator()
    if choice == 3:
        print("You have chosen option 3, the currency converter")
        currency_display()
    else:
        print("You have entered an invalid choice")


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
                 "Wanqing,", "Qianran,", "Shupei,", "Hebatalla", "Chicago,", "Kate,", "Ashton,", "Krishaan,",
                 "Jasmine,", "Steven,", "Han,", "Fredo,", "Tony,", "John,", "Walter"]
    random_choice = random.choice(name_list)  # here a random name is chosen from the list
    return str(random_choice)  # here the chosen name is returned to the poem function


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


def number_generator():
    """
    this function takes the 2 random number and multiplies the product of their squares
    """
    x = random.randint(1, 3)
    y = random.randint(2, 5)
    print(x * x * y * y)


menu()
