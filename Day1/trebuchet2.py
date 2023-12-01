# Advent of Code 2023: Day 1, task 2.
# Amy L Hewitt

'''
This code takes the first and last number of each line in a file and combines
them into an integer two digit number. This time, the numbers might be spelled
out or written as digits. Each two digit number is added together to get the
final result.

It uses the find() function to search for each valid number and return an array
containing each found number and the index of its first occurence. The array is
then sorted so that the number with the lowest index is returned as the first
digit in the two digit number. For the second digit, rfind() is used so that
each valid number is searched for from the right, and then the number with the
highest index is returned.

To run, you must have an input file named 'trebuchet-input.txt' saved in the same
directory as this script.
'''

import os
import numpy as np

# This function uses the find() function to look for the index of each valid number
def get_number(line, numbers, digit):
    if digit == 1: # If looking for the first digit, start looking from the left
        found = np.array([[int(line.find(number)), int(numbers[number])] for number in numbers if line.find(number) != -1])
        sorted = found[found[:, 0].argsort()]
        number = sorted[0][1] # Return number with the lowest index
    elif digit == 2: # If looking for the second digit, start looking from the right
        found = np.array([[int(line.rfind(number)), int(numbers[number])] for number in numbers if line.rfind(number) != -1])
        sorted = found[found[:, 0].argsort()]
        number = sorted[-1][1] # Return number with highest index
    return number

# Change working directory to current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os. chdir(dir_path)

# Read input file
with open("trebuchet-input.txt") as f:
    lines = f.readlines()

count = 0

# Define acceptable "numbers" and their values
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
    }

# Calculate sum of two digit numbers
for line in lines:
    two_digit_number = int(f"{get_number(line, numbers, digit=1)}{get_number(line, numbers, digit=2)}")
    count += two_digit_number

print(count)