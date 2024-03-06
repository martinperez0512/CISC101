"""
This program allows the user to select an item from the menu give a tip if they desire
Author: Martin Perez
Student Number: 20360377
Date: Sept 2022
"""

# Define the menu items and their prices
menu_items = ["Chicken Wrap", "Wings (10)", "Fries", "Meatball Sub", "Soup"]
prices = [4.50, 16.99, 4.59, 8.39, 2.95]

# Print the menu
print("Items available for purchase:")
for i in range(len(menu_items)):
    print("{}. {} ${:.2f}".format(i + 1, menu_items[i], prices[i]))

# Get the user's choice
while True:
    choice = int(input("Enter the number corresponding to the item that you would like to purchase: "))

    # Check if the choice is valid
    if choice < 1 or choice > len(menu_items):
        print("Invalid choice. Please try again.")
    else:
        break

# Calculate the total
total = prices[choice - 1] * 1.05  # Add 5% tax

# Ask if the user wants to add a tip
add_tip = input("Would you like to add a tip? (Y/N) ")
if add_tip.lower() == "y":
    tip_type = input("Enter the tip as a percentage or a fixed amount (P/A): ")
    if tip_type.lower() == "p":
        tip_percent = float(input("Enter the tip percentage: "))
        tip = total * tip_percent / 100
    elif tip_type.lower() == "a":
        tip = float(input("Enter the tip amount: "))
    else:
        print("Invalid tip type. No tip will be added.")
        tip = 0
else:
    tip = 0

# Print the total
print("Total: ${:.2f}".format(total + tip))
