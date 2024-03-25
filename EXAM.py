"""
I certify that this work has been done solely by myself and that I have not communicated with anyone during this
examination using any means of communication.  I understand that a breach of academic integrity on this final exam will
result in a failure in the course and possible additional consequences.

This program will work with a dictionary and list of guests for a party to complete the tasks that are asked on ONQ
Author: Martin Perez
Student Number: 20360377
Date: December 2022
"""


def initialize_guest_list():
    """
    This function crates the the guest list along with what food they are bringing and how many guests will be coming
    with them
    :returns: dictionary with all the guest information
    """
    guest_list = {"Raisa": ["pizza", "cookies", 3], "Susan": ["salad", 2], "Jia": ["ice cream", 0], "Val": ["cake", 2],
                  "Brian": ["pasta", "cheese", "crackers", 2], "Chandra": ["burgers", "buns", 3]}
    return guest_list


def get_uninvited_guests(guest_list, powley_guests):
    """
    This function takes a dictionary of guests and their food items, and a list of desired guests and returns a list of
     guests that are in the desired guest list but not in the guest list.
    :param guest_list: A dictionary of guests and their food items
    :param powley_guests: A list of desired guests
    :returns A list of guests that are in the desired guest list but not in the guest list
    """
    guests = set(guest_list.keys())  # create a set of guests in the guest list

    uninvited = []  # creates a list of uninvited guests
    for guest in powley_guests:
        if guest not in guests:
            uninvited.append(guest)

    return uninvited


def add_to_guest_list(guest_list, powley_guests):
    """
    This function will take the names from powley_guests that are not in the guest list dictionary and add them to the
    dictionary with the food item saying "TBD" and the additional guests being 0.
    :param guest_list: A dictionary of guests and their food items
    :param powley_guests: A list of desired guests
    :return: updated guest_list dictionary with the new info
    """
    guests = set(guest_list.keys())  # create a set of guests in the guest list

    for guest in powley_guests:
        if guest not in guests:
            guest_list[guest] = ["TBD", 0]
    return guest_list


def guest_list_check(guest_list):
    """
    This function checks for the conditions in the assignment and will print either "True" or "False" if those
    conditions are met or not in the guest list
    :param guest_list:  A dictionary of guests and their food items
    """
    for i in guest_list:  # checks all the names in the dictionary
        food_item = guest_list[i][0]
        num_guests = guest_list[i][-1]
        if num_guests > 0 and (len(food_item) > 3 or food_item[0] == 'p'):  # checks first condition
            print("True")
        elif num_guests == 0 and "s" in food_item and "p" in food_item:  # checks second condition
            print("True")
        else:
            print("False")


def add_new_guests(powley_list):
    """
    This function will ask the user how many new names they want to add to Powley's list and checks if the entered name
    is already in the list, if it is not then it is added and finally it will print the updated list.
    :param powley_list: A list of desired guests
    :return:
    """
    powley_guests = []  # new empty list

    num_names = int(input("How many names do you want to enter? "))  # ask the user how many names they want to enter

    while len(powley_guests) < num_names:  # keep asking for names until we have the desired number of names
        name = input("Enter a name: ")
        if name not in powley_list:
            powley_guests.append(name)
        else:
            print("This name is already in the guest list. Please enter another name.")

    new_list = powley_list + powley_guests
    print("Here is the new list with the added names:\n", new_list)  # prints the new list with original names included


def main():
    """
    This is the main function where all the other functions are called.
    """
    info = initialize_guest_list()
    powley_guests = ["Isla", "Susan", "Ellen", "Jia", "Raisa", "Chandra", "Wendy"]
    for name, items in info.items():  # prints the guest and food they will bring
        food_items = items[:-1]  # gets list of food items without the number of guests
        food_string = " and ".join(food_items)  # adds other food items with "and" if they have more than one
        print(f"{name} is bringing {food_string}.")
    print()

    num_guests = 6  # counts the number of guests (starts at 6 since they are the ones bringing the additional guests)
    for name, items in info.items():
        num_guests += items[-1]  # adds the number of guests to the total
    print(f"There will be a total of {num_guests} guests at the party.")
    print()

    show_uninvited_guests = get_uninvited_guests(info, powley_guests)
    print("The guests who were in powley_guests, but not in the original guest list were:\n", show_uninvited_guests)
    print()

    add_uninvited_guests = add_to_guest_list(info, powley_guests)
    print("Here is the updated guest list:")
    for name, items in add_uninvited_guests.items():  # prints the guest and food they will bring
        food_items = items[:-1]  # gets list of food items without the number of guests
        food_string = " and ".join(food_items)  # adds other food items with "and" if they have more than one
        print(f"{name} is bringing {food_string}.")
    print()

    guest_list_check(info)
    print()

    add_new_guests(powley_guests)


main()
