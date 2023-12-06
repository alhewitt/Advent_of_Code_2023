# Advent of Code 2023: Day 2, task 1.
# Amy L Hewitt

'''
This code takes in a series of "games" in which an arbitrary number of
cubes are pulled out of a hat three times. It then checks whether each
game would be possible with:
12 red cubes,
13 green cubes,
14 blue cubes.

To run, you must have an input file named 'input.txt' saved in the same
directory as this script.
'''

import os
import numpy as np

def get_sets(game):
    num = game.split(':')[0].lstrip('Game ')
    sets = [x for x in game.split(': ')[1].split('; ')]
    valid = 0
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
        if colours[0] > 12 or colours[1] > 13 or colours[2] > 14:
            valid = 1
    return num, valid

# Change working directory to current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os. chdir(dir_path)

# Read input file
with open("input.txt") as f:
    games = f.readlines()

# Check whether each game is possible
total = 0
for game in games:
    game_validity = get_sets(game)
    if game_validity[1] == 0:
        total += int(game_validity[0])
print(total)