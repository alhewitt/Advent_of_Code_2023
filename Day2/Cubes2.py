# Advent of Code 2023: Day 2, task 2.
# Amy L Hewitt

'''
This code takes in a series of "games" in which an arbitrary number of
cubes are pulled out of a hat three times. It then checks what the least
number of each colour cube could have been in the hat and calculates the
product of each of those amounts. It returns the sum of these products.

To run, you must have an input file named 'input.txt' saved in the same
directory as this script.
'''

import os
import numpy as np

def get_sets(game):
    num = game.split(':')[0].lstrip('Game ')
    sets = [x for x in game.split(': ')[1].split('; ')]
    valid = 0
    min_colours = [0, 0, 0]
    for set in sets:
        colours = np.zeros(3)
        results = set.split(', ')
        for result in results:
            if 'red' in result:
                colours[0] = result.split()[0]
            elif 'green' in result:
                colours[1] = result.split()[0]
            elif 'blue' in result:
                colours[2] = result.split()[0]
        for i in range(3):
            if colours[i] > min_colours[i]:
                min_colours[i] = colours[i]
    return min_colours

# Change working directory to current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os. chdir(dir_path)

# Read input file
with open("input.txt") as f:
    games = f.readlines()

# Check whether each game is possible
total = 0
for game in games:
    min_colours = get_sets(game)
    power = np.prod(min_colours)
    total += power
print(total)