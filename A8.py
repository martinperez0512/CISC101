"""
This program tk
Author: Martin Perez
Student Number: 20360377
Date: November 2022
"""

import urllib.request
import os


def read_words(url):
    try:
        # Open a connection to the website
        response = urllib.request.urlopen(url)

        # Read the data as a string
        data = response.read().decode('utf-8')

        # Split the string into a list of words
        words = data.split()

        # Return the list of words
        return words
    except:
        # If something goes wrong, inform the user and return an empty list
        print("Failed to read words from URL:", url)
        return []


def word_count(word_list):
    # Initialize an empty dictionary
    counts = {}

    # Loop through the list of words
    for word in word_list:
        # Count the number of letters in the word
        num_letters = len(word)

        # If the dictionary already contains a key for this number of letters, increment the value
        if num_letters in counts:
            counts[num_letters] += 1
        # Otherwise, add a new key/value pair to the dictionary
        else:
            counts[num_letters] = 1

    # Return the dictionary
    return counts


def total_words(counts, n, m):
    # Initialize a variable to store the total number of words
    total = 0

    # Loop through the dictionary
    for length, num_words in counts.items():
        # If the length is between n and m (inclusive), add the number of words to the total
        if n <= length <= m:
            total += num_words

    # Return the total number of words
    return total


def max_frequency(counts):
    # Initialize a variable to store the maximum frequency
    max_freq = 0

    # Loop through the dictionary
    for length, num_words in counts.items():
        # If the number of words is greater than the current maximum, update the maximum
        if num_words > max_freq:
            max_freq = num_words

    # Return the maximum frequency
    return max_freq


def max_word_length(counts):
    # Initialize a variable to store the maximum word length
    max_length = 0

    # Loop through the dictionary
    for length, num_words in counts.items():
        # If the length is greater than the current maximum, update the maximum
        if length > max_length:
            max_length = length

    # Return the maximum word length
    return max_length


def write_to_file(counts):
    # Open the file in write mode
    with open("statWords.txt", "w") as file:
        # Loop through the dictionary
        for length, num_words in counts.items():
            # Create a string describing the number of words of this length
            line = "There are {} words of length {}".format(num_words, length)

            # Write the string to the file, followed by a newline character
            file.write(line + os.linesep)


def main():
    # Read the words from the website
    words = read_words("https://research.cs.queensu.ca/home/cords2/words.txt")

    # Count the words by length
    counts = word_count(words)

    # Calculate the total number of words of lengths 1 to 2
    total1 = total_words(counts, 1, 2)
    print("Total number of words of lengths 1 to 2:", total1)

    # Calculate the total number of words of lengths 3 to 6
    total2 = total_words(counts, 3, 6)
    print("Total number of words of lengths 3 to 6:", total2)

    # Print the maximum word length and frequency
    max_length = max_word_length(counts)
    print("Maximum word length:", max_length)
    max_freq = max_frequency(counts)
    print("Length with maximum frequency:", max_freq)

    # Write the word counts to a file
    write_to_file(counts)


main()
