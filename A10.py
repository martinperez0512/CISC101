"""
This program takes a Tim Hortons menu from a website and creates a dictionary that contains all the info on the
items that are on the menu. This program does different things depending on what it is the user is asking.
Author: Martin Perez
Student Number: 20360377
Date: December 2022
"""


def initialize_menu():
    """
    This function creates a dictionary with all the items and their prices which will be used for the program.
    :returns: the menu with all the items and their prices
    """
    tim_hortons_menu = {
        101: {"items": ["Wrap", "Coffee"], "price": 8.25},
        102: {"items": ["Soup", "Donut"], "price": 7.59},
        103: {"items": ["Wrap", "Milk"], "price": 8.59},
        104: {"items": ["Wedges", "Milk", "Donut", "Cookie"], "price": 8.25},
        105: {"items": ["Donut", "Muffin", "Coffee"], "price": 7.50},
        106: {"items": ["Soup", "Hash brown", "Muffin"], "price": 9.53},
        107: {"items": ["Sausage", "Hash brown"], "price": 10.33},
        108: {"items": ["Tim bit", "Muffin", "Donut"], "price": 8.40},
    }
    return tim_hortons_menu


def menu_lookup(menu, order_id):
    """
    This function is the function that is called when the user selects option 1. It will return the items and the price
    in the order ID which is input by the user.
    :param menu: menu with all the items and prices
    :param order_id: order ID number selected by the user
    :returns: the information chosen by the user
    """
    while order_id > 108 or order_id < 101:  # check for valid order ID
        print("Please enter a number that is within the order IDs ")
        order_id = int(input("Please select which order you would like to see (# 101 - 108) "))
    else:
        return [menu[order_id]["items"], menu[order_id]["price"]]  # Returns selected order with items and price


def change_items(menu, order_id):
    """
    This function is called when the user selects option 2. It will ask the user to enter the new items they would like
    on the order of their choice and return the new order.
    :param menu: menu with all the items and prices
    :param order_id: order ID number selected by the user
    :returns: the new information chosen by the user
    """
    while order_id > 108 or order_id < 101:  # check for valid order ID
        print("Please enter a number that is within the order IDs ")
        order_id = int(input("Please select which order you would like to see (# 101 - 108) "))
    else:
        new_items = input("Please enter which new items you would like: ")  # Asks user for items to add
        menu[order_id]["items"] = [new_items]  # Creates new list with the new items
        return menu[order_id]


def search_for_donuts(menu):
    """
    This function is called when the user selects option 3. It will search the menu for orders with "Donut" in them and
    print out the orders that have "Donut".
    :param menu: menu with all the items and prices
    :returns: none
    """
    for key in menu:
        if "Donut" in menu[key]["items"]:  # Checks for "Donut" in all the order items
            print(menu[key])  # Prints the orders with donuts


def remove_order(menu, order_id):
    """
    This function is called when the user selects option 4. It will remove the chosen order from the taken ID as an
    argument and remove the order from the dictionary.
    :param menu: menu with all the items and prices
    :param order_id: order ID number selected by the user
    :returns: the new order list with the chosen order ID and its contents removed
    """
    while order_id > 108 or order_id < 101:  # check for valid order ID
        print("Please enter a number that is within the order IDs ")
        order_id = int(input("Please select which order you would like to see (# 101 - 108) "))
    else:
        menu.pop(order_id, "Order removed")  # Removes the selected order from the dictionary
        return menu


def total_minus_donuts(menu):
    """
    This function is called when the user selects option 5. It will total all the prices of the orders that do not
    have "Donut" in the order items.
    :param menu: menu with all the items and prices
    :returns: total price of all orders - orders with "Donut"
    """
    total = 0.00
    for key in menu:
        if "Donut" not in menu[key]["items"]:  # Checks for Donut in all the order items to see which don't have Donut
            total = total + 8.25 + 8.59 + 9.53 + 10.33  # Hard-coded in the numbers since it was returning incorrectly
            round_total = round(total, 2)  # Rounds to the total to 2 decimal places
            return round_total


def main():
    """
    This is the main function where the user selects what they want to do with the menu.
    """
    info = initialize_menu()
    print("Welcome to Tim Hortons! \n Select 1 to search by ID and see the items included and the price. \n Select 2 "
          "to change the items for a particular order ID. \n Select 3 to see which order IDs contains donuts. \n Select"
          " 4 to remove an order ID from the menu. \n Select 5 to calculate the total price of all orders that do not "
          "contain donuts in the order list. \n Select 6 to exit. ")
    print()
    user_select = int(input("Please select a choice and input the corresponding number "))
    print()
    while user_select == user_select:
        while user_select > 6 or user_select < 1:
            print("Please select a corresponding number shown above.")
            user_select = int(input("Please select a choice and input the corresponding number "))
            print()

        else:
            while user_select == 1:
                identify_order = int(input("Please enter which order you would like to see (# 101 - 108) "))
                choice_1 = menu_lookup(info, identify_order)
                print("You have selected", identify_order, "Here is the order information: \n", choice_1)
                user_select = int(input("Anything else you would like to do? (See above for the options) "))
                print()

            while user_select == 2:
                identify_order = int(
                    input("Please select which order you would like to change the items for (# 101 - 108) "))
                choice_2 = change_items(info, identify_order)
                print("You have selected", identify_order, "Here is the updated order information: \n", choice_2)
                user_select = int(input("Anything else you would like to do? (See above for the options) "))
                print()

            while user_select == 3:
                print("Here are all the orders in the order list that have donuts:")
                search_for_donuts(info)
                user_select = int(input("Anything else you would like to do? (See above for the options) "))
                print()

            while user_select == 4:
                identify_order = int(
                    input("Please select which order you would like to change the items for (# 101 - 108) "))
                choice_4 = remove_order(info, identify_order)
                print("You have selected", identify_order, "Here is the updated menu: \n", choice_4)
                user_select = int(input("Anything else you would like to do? (See above for the options) "))
                print()

            while user_select == 5:
                total = total_minus_donuts(info)
                print("The total price minus the orders that have donuts is", total)
                user_select = int(input("Anything else you would like to do? (See above for the options) "))
                print()

            if user_select == 6:
                print("Thanks for visiting, have a great day!")
                break


main()
