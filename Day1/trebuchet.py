# Advent of Code 2023: Day 1, task 1.
# Amy L Hewitt

'''
This code takes the first and last numerical digit of each line in a file
and combines them into an integer two digit number. Each number is added
together to get the final result.

To run, you must have an input file named 'trebuchet-input.txt' saves in
the same directory as this script.
'''

import os

# Change working directory to current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os. chdir(dir_path)

# Read input file
with open("trebuchet-input.txt") as f:
    lines = f.readlines()

count = 0

# Calculate sum of two digit numbers
for line in lines:
    digits = [int(x) for x in line if x.isdigit()]
    count += int(f"{digits[0]}{digits[-1]}")

print(count)