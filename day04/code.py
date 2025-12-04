import os.path
import re


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines


class Dummy:
    def __init__(self):
        self.dummy = 0

    def setup(self, input):
        for set in re.findall(r"[^;]+", input):
            pass


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

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    numbers = [[int(x) for x in re.findall(r"\d+", line)] for line in input]
    return 0


def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    return 0


if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
