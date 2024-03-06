"""
This program allows the user to input a number grade and outputs the equivalent letter grade
According to the Queen's University grading scale
Author: Martin Perez
Student Number: 20360377
Date: Sept 2022
"""

# Define the letter grades and their corresponding ranges
letter_grades = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
grade_ranges = [0, 50, 52, 55, 59, 62, 66, 69, 72, 76, 79, 84, 89, 100]

# Get the user's grade
grade = float(input("Enter your numerical grade: "))

# Check if the grade is in the valid range
if grade < 0 or grade > 100:
    print("The grade is out of range.")
else:
    # Find the corresponding letter grade
    for i in range(len(grade_ranges) - 1):
        if grade >= grade_ranges[i] and grade < grade_ranges[i + 1]:
            print("Your letter grade is: {}".format(letter_grades[i]))
            break
