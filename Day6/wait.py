# Advent of Code 2023: Day 6, task 1.
# Amy L Hewitt

'''
This code takes in a series of races in which a boat needs to travel further
than the current record holder. To speed up the boat, a button is held down
which increases the speed of the boat by 1 ms per ms. This counts as part of
the time limit. For each race, there may be multiple ways to beat the high
score. The number of ways for each race is multiplied together to get the
output.

For part 2 of this challenge, input.txt has been modified to be correct.

To run, you must have an input file named 'input.txt' saved in the same
directory as this script.
'''

import os
import numpy as np

# Change working directory to current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os. chdir(dir_path)

# Read input file
with open("input.txt") as f:
    cols = f.readlines()

result = 1
for i in range(1,len(cols[0].split())):
    time = int(cols[0].split()[i])
    record = int(cols[1].split()[i])
    wins = 0
    for time_held in range(time+1):
        speed = time_held
        time_left = time-time_held
        distance = speed * time_left
        if distance > record:
            wins += 1
    result *= wins
print(result)

