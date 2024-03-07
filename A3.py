"""
This program is a dice game that depending on the result, will do something different
Author: Martin Perez
Student Number: 20360377
Date: Sept 2022
"""
import random

# Print the welcome message
print("Welcome to the very fun dice game.")

# Define the initial points total
points = 0

# Flag variable to stop the game
stop_play = False

# Outer loop to keep playing the game
while not stop_play:
    # Roll the dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("You have rolled ", die1, die2)

    # Check for condition 1: doubles
    if die1 == die2:
        print("You have rolled doubles.")
        num_rolls = 0
        while die1 == die2:
            die2 = random.randint(1, 6)
            num_rolls += 1
            print("Dice currently are: ", die1, die2)
        points += die1 + die2 + num_rolls
        print("You have", points, "points")
    # Check for condition 2: sum of dice is even
    elif (die1 + die2) % 2 == 0:
        print("The sum of", die1, die2, "is even so rolling the dice 4 times")
        for i in range(4):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print("Dice currently are: ", die1, die2)
            points += die1 + die2
        print("You have", points, "points")
    # Check for condition 3: one die is 3
    elif die1 == 3 or die2 == 3:
        print("One of the dice is 3 so adding 3 to the points total")
        points += 3
        print("You have", points, "points")
        stop_play = True
    # Check for condition 4: sum of dice is 7
    elif die1 + die2 == 7:
        print("The sum of the dice is 7 which is magic so adding 10 points to the total")
        points += 10
        for i in range(10):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            points += die1 + die2
        print("You have", points, "points")
    # None of the conditions are satisfied
    else:
        points += die1 + die2
        print("You have", points, "points")

    # Ask the user if they want to continue playing
    if not stop_play:
        continue_playing = input(
            "Do you wish to continue to play the game and get more points?"
            " (Enter Y/y to continue or any other character to end ")
        if continue_playing.lower() != "y":
            stop_play = True

# Game over
print("Game over.")
