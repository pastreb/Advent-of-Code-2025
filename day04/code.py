import os.path
import re


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines

# --- Day 4: Printing Department ---

# You ride the escalator down to the printing department. They're clearly 
# getting ready for Christmas; they have lots of large rolls of paper 
# everywhere, and there's even a massive printer in the corner (to handle the 
# really big print jobs).

# Decorating here will be easy: they can make their own decorations. What you 
# really need is a way to get further into the North Pole base while the 
# elevators are offline.

# "Actually, maybe we can help with that," one of the Elves replies when you 
# ask for help. "We're pretty sure there's a cafeteria on the other side of 
# the back wall. If we could break through the wall, you'd be able to keep 
# moving. It's too bad all of our forklifts are so busy moving those big 
# rolls of paper around."

# If you can optimize the work the forklifts are doing, maybe they would have 
# time to spare to break through the wall.

# The rolls of paper (@) are arranged on a large grid; the Elves even have a 
# helpful diagram (your puzzle input) indicating where everything is located.

# For example:

# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.

# The forklifts can only access a roll of paper if there are fewer than four 
# rolls of paper in the eight adjacent positions. If you can figure out which 
# rolls of paper the forklifts can access, they'll spend less time looking 
# and more time breaking down the wall to the cafeteria.

# In this example, there are 13 rolls of paper that can be accessed by a 
# forklift (marked with x):

# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.

# Consider your complete diagram of the paper roll locations. How many rolls 
# of paper can be accessed by a forklift?

def count_neighbor_rolls(map, i, j):
    neighborhood = [row[max(j-1,0):min(len(row),j+2)] for row in map[max(0,i-1):min(len(map),i+2)]]
    return sum(sum(cell.count('@') for cell in row) for row in neighborhood) - 1 if map[i][j] == '@' else 0

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    map = [[x for x in re.findall(r"\.|\@", line)] for line in input]
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            count += map[i][j] == '@' and count_neighbor_rolls(map, i, j) < 4
    return count

# 1376
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

# --- Part Two ---

# Now, the Elves just need help accessing as much of the paper as they can.

# Once a roll of paper can be accessed by a forklift, it can be removed. Once 
# a roll of paper is removed, the forklifts might be able to access more 
# rolls of paper, which they might also be able to remove. How many total 
# rolls of paper could the Elves remove if they keep repeating this process?

# Starting with the same example as above, here is one way you could remove 
# as many rolls of paper as possible, using highlighted @ to indicate that a 
# roll of paper is about to be removed, and using x to indicate that a roll 
# of paper was just removed:

# Initial state:
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.

# Remove 13 rolls of paper:
# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.

# Remove 12 rolls of paper:
# .......x..
# .@@.x.x.@x
# x@@@@...@@
# x.@@@@..x.
# .@.@@@@.x.
# .x@@@@@@.x
# .x.@.@.@@@
# ..@@@.@@@@
# .x@@@@@@@.
# ....@@@...

# Remove 7 rolls of paper:
# ..........
# .x@.....x.
# .@@@@...xx
# ..@@@@....
# .x.@@@@...
# ..@@@@@@..
# ...@.@.@@x
# ..@@@.@@@@
# ..x@@@@@@.
# ....@@@...

# Remove 5 rolls of paper:
# ..........
# ..x.......
# .x@@@.....
# ..@@@@....
# ...@@@@...
# ..x@@@@@..
# ...@.@.@@.
# ..x@@.@@@x
# ...@@@@@@.
# ....@@@...

# Remove 2 rolls of paper:
# ..........
# ..........
# ..x@@.....
# ..@@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@x.
# ....@@@...

# Remove 1 roll of paper:
# ..........
# ..........
# ...@@.....
# ..x@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...

# Remove 1 roll of paper:
# ..........
# ..........
# ...x@.....
# ...@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...

# Remove 1 roll of paper:
# ..........
# ..........
# ....x.....
# ...@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...

# Remove 1 roll of paper:
# ..........
# ..........
# ..........
# ...x@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...

# Stop once no more rolls of paper are accessible by a forklift. In this 
# example, a total of 43 rolls of paper can be removed.

# Start with your original diagram. How many rolls of paper in total can be 
# removed by the Elves and their forklifts?

def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    map = [[x for x in re.findall(r"\.|\@", line)] for line in input]
    total = 0
    while True:
        count = 0
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '@' and count_neighbor_rolls(map, i, j) < 4:
                    count += 1
                    map[i][j] = '.'
        if count == 0:
            break
        total += count
    return total

# 8587
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
