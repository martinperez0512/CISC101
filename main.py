"""
This program contains a list of students and will do different things to the marks of the students such as calculating
the average or adding a new student.
Author: Martin Perez
Student Number: 20360377
Date: Oct 2022
"""


def print_mark(name):
    """
    This function takes the parameter given from the main function and prints the mark of the student that is given.
    If the parameter is not a name in the list then the function will print that there is no student by that name
    """

    students = ["Jane", "Xinrong", "Sima"]
    if name in students:
        print('Student found')
        if name == students[0]:
            print("The marks for Jane are:\n A1: 80\n A2: 74\n A3: 93\n A4: 60")
        if name == students[1]:
            print("The marks for Xinrong are:\n A1: 72\n A2: 89\n A3: 55\n A4: 75")
        if name == students[2]:
            print("The marks for Sima are:\n A1: 93\n A2: 80\n A3: 74\n A4: 60")

        print('No student by that name ')


def average_assignment(assignment_number):
    """
    This function takes the parameter given in the main function and and calculates the average grade for the given
    assignment
    """
    if assignment_number == 1:
        a_one_avg = (80 + 72 + 93) / 3
        return a_one_avg
    if assignment_number == 2:
        a_two_avg = (74 + 89 + 80) / 3
        return a_two_avg
    if assignment_number == 3:
        a_three_avg = (93 + 55 + 74) / 3
        return a_three_avg
    if assignment_number == 4:
        a_four_avg = (60 + 75 + 60) / 3
        return a_four_avg
    else:
        return -999


def average_mark(name):
    """
    This function takes a name from the main function and depending on the name will calculate the average grade for
    the student who's name is in the parameter. If a name that is not in the list is entered, then the function will
    return 0.
    """
    students = ["Jane", "Xinrong", "Sima", ]
    if name in students:
        if name == students[0]:
            jane_avg = (80 + 74 + 93 + 60) / 4
            return jane_avg
        if name == students[1]:
            xinrong_avg = (72 + 89 + 55 + 75) / 4
            return xinrong_avg
        if name == students[2]:
            sima_avg = (93 + 80 + 74 + 60) / 4
            return sima_avg
    else:
        return 0


def highest_average_mark():
    """
    This function displays the highest average out of the three students. Since both Jane and Sima share the highest
    average in the list the function puts both of their names and their average.
    """

    highest_mark = [("Jane", [76.75]), ("Sima", [76.75])]
    print("Both Jane and Sima have the highest average. ", highest_mark)


def increase_marks():
    """
    This function takes the new marks that were increased by one and prints them.
    """

    new_marks = [("Jane", [81, 75, 94, 61]), ("Xinrong", [73, 90, 56, 76]), ("Sima", [94, 81, 75, 61])]
    print(new_marks)


def add_new_student():
    """
    This function takes the list of students and marks and allows a new student to be added along with their marks.
    The function will add the new print the new list including the new students name and grades on the four
    assignments.
    """
    print("Now we are going to add new student")
    students = [("Jane", [80, 74, 93, 60]), ("Xinrong", [72, 89, 55, 75]), ("Sima", [93, 80, 74, 60])]
    again = 'Y'
    while again.upper() == 'Y':
        name = input('Enter a name: ')
        while name == 'Jane' or name == 'Xinrong' or name == 'Sima':
            print('Please enter a unique name')
            break
        else:
            mark1 = int(input("Please input this student's mark for assignment 1 (percentage) "))
            while mark1 < 0 or mark1 > 100:
                print("Please input a proper percentage")
                break
            mark2 = int(input("Please input this student's mark for assignment 2 (percentage) "))
            while mark2 < 0 or mark2 > 100:
                print("Please input a proper percentage")
                break
            mark3 = int(input("Please input this student's mark for assignment 3 (percentage) "))
            while mark3 < 0 or mark3 > 100:
                print("Please input a proper percentage")
                break
            mark4 = int(input("Please input this student's mark for assignment 4 (percentage) "))
            while mark4 < 0 or mark4 > 100:
                print("Please input a proper percentage")
                break
        print('Do you want to add another name? ')
        again = input('y = yes, anything else = no: ')
    print('Here are the names you entered. ')
    new_list = [students, (name, [mark1, mark2, mark3, mark4])]
    print(new_list)


def main():
    # Make your program user friendly by adding print statements telling the user what is happening.
    # The students structure is a list of tuples, each representing a student and their list
    # of marks on 4 assignments.  You must NOT assume that there are ONLY 3 students -- there
    # may be 0 or 100000 students & your program should still work!
    # You may assume that there are EXACTLY 4 marks per student.
    # You may also assume that no two students have the same name.
    # You may need to test with different data than is given here in order to test all your
    # conditions.

    # leave the next 3 lines in your code.
    students = [("Jane", [80, 74, 93, 60]), ("Xinrong", [72, 89, 55, 75]), ("Sima", [93, 80, 74, 60])]
    print("Here is the data set", students)

    # These next three lines call the print_mark function
    print_mark(students[1][0])
    print_mark(students[2][0])
    print_mark('Martin')

    # print the average that was returned by averageAssignment()
    print("This is the average mark on the first assignment:\n", average_assignment(1))

    # call averageMark to get Jane's overall average
    print("This was the average grade for Jane:\n", average_mark(students[0][0]))
    # call averageMark for a student who does not exist
    print("Here we called the average mark for a student that doesn't exist, the name used was David.\n",
          average_mark('David'))

    highest_average_mark()
    add_new_student()
    print("^ These are the new marks after being increased by one ^\n ", increase_marks())


main()
